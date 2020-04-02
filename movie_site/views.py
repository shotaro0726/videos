from django.shortcuts import resolve_url, get_object_or_404, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, FormView, UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .models import Movie, MovieComment
from .forms import MovieUploadForm, MovieCommentCrateForm


class MovieTopListView(ListView):
    template_name = "movie_site/movie_list.html"
    model = Movie
    paginate_by = 5


class MovieDetailView(DetailView):
    template_name = "movie_site/movie_detail.html"
    model = Movie


class MovieFormView(LoginRequiredMixin, FormView):
    template_name = 'movie_site/movie_form.html'
    model = Movie
    form_class = MovieUploadForm
    success_url = reverse_lazy("movie_site:movie_top")

    def form_valid(self, form):
        movie = form.save(commit=False)
        movie.user = self.request.user
        movie.save()
        messages.success(self.request, '投稿しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "投稿に失敗しました。")
        return super().form_invalid(form)


class MovieUpdateView(LoginRequiredMixin, UpdateView):
    model = Movie
    form_class = MovieUploadForm
    template_name = 'movie_site/movie_update_form.html'

    def get_success_url(self):
        return resolve_url('movie_site:movie_detail', pk=self.kwargs['pk'])

    def form_valid(self, form):
        messages.success(self.request, "動画を更新しました!")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "動画内容の更新に失敗しました。")
        return super().form_invalid(form)


class MovieDeleteView(LoginRequiredMixin, DeleteView):
    model = Movie
    success_url = reverse_lazy("movie_site:movie_top")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "動画を削除しました。")
        return super().delete(request, *args, **kwargs)


class MovieCommentView(CreateView):
    model = MovieComment
    form_class = MovieCommentCrateForm
    template_name = 'movie_site/movie_comment_form.html'

    def form_valid(self, form):
        movie_pk = self.kwargs['pk']
        movie = get_object_or_404(Movie, pk=movie_pk)

        comment = form.save(commit=False)
        comment.target = movie
        comment.save()
        return redirect('movie_site:movie_detail', pk=movie_pk)


class MovieSearchView(ListView):
    model = Movie
    paginate_by = 5
    template_name = 'movie_site/movie_search_form.html'

    def get_queryset(self):
        queryset = Movie.objects.order_by('-created_at')
        keyword = self.request.GET.get('keyword')
        if keyword:
            queryset = queryset.filter(
                Q(title__icontains=keyword) | Q(setsumei__icontains=keyword))
            messages.success(self.request, '「{}」の検索結果'.format(keyword))
        return queryset


class MovieUserPageView(ListView):
    model = Movie
    template_name = 'movie_site/movie_userpage.html'
    paginate_by = 5

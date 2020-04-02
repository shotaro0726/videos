from django.urls import path
from .views import MovieTopListView, MovieDetailView, MovieFormView, MovieUpdateView, MovieDeleteView, MovieCommentView, \
    MovieSearchView, MovieUserPageView
from django.conf.urls.static import static
from django.conf import settings

app_name = 'movie_site'

urlpatterns = [
    path('', MovieTopListView.as_view(), name='movie_top'),
    path('detail/<int:pk>', MovieDetailView.as_view(), name='movie_detail'),
    path('upload', MovieFormView.as_view(), name='movie_upload'),
    path('update/<int:pk>', MovieUpdateView.as_view(), name='movie_update'),
    path('delete/<int:pk>', MovieDeleteView.as_view(), name='movie_delete'),
    path('comment/<int:pk>', MovieCommentView.as_view(), name='movie_comment'),
    path('search_list/', MovieSearchView.as_view(), name='movie_search'),
    path('user_page/',MovieUserPageView.as_view(),name='movie_user'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

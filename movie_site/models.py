from django.db import models


class Movie(models.Model):
    title = models.CharField('動画のタイトル', max_length=255)
    setsumei = models.CharField('動画の説明 ※空白可', max_length=500, blank=True)
    samune = models.ImageField(
        'サムネイル ※空白可', upload_to='samune/', null=True, blank=True)
    upload = models.FileField('動画ファイル', upload_to="uploads/%Y/%m/%d/")
    created_at = models.DateTimeField('作成日', auto_now_add=True)
    updated_at = models.DateTimeField('更新日', auto_now=True)

    def __str__(self):
        return self.title


class MovieComment(models.Model):
    name = models.CharField('お名前', max_length=80)
    text = models.CharField('コメント', max_length=500)
    target = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

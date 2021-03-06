# Generated by Django 3.0.3 on 2020-04-05 01:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='動画のタイトル')),
                ('setsumei', models.CharField(blank=True, max_length=500, verbose_name='動画の説明 ※空白可')),
                ('samune', models.ImageField(blank=True, null=True, upload_to='samune/', verbose_name='サムネイル ※空白可')),
                ('upload', models.FileField(upload_to='uploads/%Y/%m/%d/', verbose_name='動画ファイル')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
            ],
        ),
        migrations.CreateModel(
            name='MovieComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='お名前')),
                ('text', models.CharField(max_length=500, verbose_name='コメント')),
                ('target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie_site.Movie')),
            ],
        ),
    ]

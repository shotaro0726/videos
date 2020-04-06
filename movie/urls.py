"""movie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.staticfiles.urls import static
from django.urls import path, include

from . import settings_dev #開発環境用をインポート

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movie_site.urls')),
    path('accounts/', include('allauth.urls')),
]

#開発環境用のルートをセット
urlpatterns += static(settings_dev.MEDIA_URL, document_root=settings_dev.MEDIA_ROOT)

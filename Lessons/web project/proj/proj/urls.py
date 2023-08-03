"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app.views import show_first_post, show_second_post, show_post, show_all_posts

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('first/', show_first_post),
    path('second/', show_second_post),
    path('posts/<int:post_id>', show_post, name="post"),
    path('posts/', show_all_posts, name='posts'),

    path("catalog/", catalog, name="catalog"),
    path("basket/", basket, name="basket"),
    path("catalog/item/<str:item_name>", item, name="item")
    /catalog/item/name1
    /catalog/item/name2
    /catalog/item/name3
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.contrib import admin
from django.urls import path
from blog.views import home, create_post, post_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('create/', create_post),
    path('post/<int:post_id>/', post_page)
]



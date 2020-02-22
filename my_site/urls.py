from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from p_library import views

from allauth.socialaccount.models import SocialAccount  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index/', views.index),
    path('publisher/', views.publisher),
    path('index/book_increment/', views.book_increment),
    path('index/book_decrrement/', views.book_decrement),
    path('accounts/', include('allauth.urls')),
    url(r'^', include('p_library.urls', namespace='p_library')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
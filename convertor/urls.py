from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index,name="index"),
    # path('about',views.about,name="about"),
    # path('result',views.result,name='result'),
    # path('fileconvertor',views.fileconvertor,name='fileconvertor'),
    # path('imageconvertor',views.imageconvertor,name='imageconvertor'),
    # path('bg',views.backgroundremover,name='backgroundremover'),
    # path('about',views.about,name="about")
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
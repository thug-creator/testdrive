from django.contrib import admin
from myapp import views
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', views.about),
    path('testdrive/', views.testdrive),
]

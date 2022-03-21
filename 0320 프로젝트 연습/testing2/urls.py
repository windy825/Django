
from django.contrib import admin
from django.urls import path, include
from article import views




urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('greeting/', views.greeting),
    path('throw/', views.throw),
    path('catch/', views.catch),
    path('hello/<int:pk>', views.hello),
]
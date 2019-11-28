from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='words-index'),
    path('about/', views.about, name="words-about")
]

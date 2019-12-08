from django.urls import path
from .views import (
    WordListView,
    WordDetailView,
    WordCreateView,
    WordUpdateView,
    WordDeleteView
)
from . import views

urlpatterns = [
    path('', WordListView.as_view(), name='words-index'),
    path('word/<int:pk>/', WordDetailView.as_view(), name='words-detail'),
    path('word/new/', WordCreateView.as_view(), name='words-create'),
    path('word/<int:pk>/update/', WordUpdateView.as_view(), name='words-update'),
    path('word/<int:pk>/delete/', WordDeleteView.as_view(), name='words-delete'),
    path('about/', views.about, name="words-about")
]

from django.urls import include, path
# from .views import WordsView
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
        path('', include(router.urls))
]

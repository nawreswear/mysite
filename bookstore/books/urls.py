from rest_framework import routers
from books.views import BookViewSet
from django.urls import path
from django.urls import include

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
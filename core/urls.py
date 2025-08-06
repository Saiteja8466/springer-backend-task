from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import home, BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', home, name='home'),
    path('', include(router.urls)),
]

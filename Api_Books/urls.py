from rest_framework import routers
from .api import BookViewSet, AuthorViewSet

router = routers.DefaultRouter()

router.register('api/books', BookViewSet, 'books')
router.register('api/authors', AuthorViewSet, 'authors')

urlpatterns = router.urls
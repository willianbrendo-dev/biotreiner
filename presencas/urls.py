from rest_framework.routers import DefaultRouter
from .views import PresencaViewSet

router = DefaultRouter()
router.register(r'presencas', PresencaViewSet, basename='presenca')

urlpatterns = router.urls

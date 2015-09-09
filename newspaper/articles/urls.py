from rest_framework.routers import DefaultRouter

from newspaper.articles.api import ArticleViewSet, ReporterViewSet

router = DefaultRouter()
router.register(r'reporters', ReporterViewSet)
router.register(r'articles', ArticleViewSet)


urlpatterns = router.urls

from rest_framework.routers import SimpleRouter

from posts.views import PostViewSet

router = SimpleRouter()
router.register("posts", PostViewSet, basename="posts")

urlpatterns = router.urls

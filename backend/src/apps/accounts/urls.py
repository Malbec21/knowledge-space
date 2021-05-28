from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from src.apps.accounts.views import (
    ExpandedTokenObtainPairView,
    RegisterViewSet,
    UserProfileViewSet,
    WorkPlaceView,
)

router = DefaultRouter()
router.register(r"accounts", RegisterViewSet, basename="accounts")
router.register(r"accounts", UserProfileViewSet, basename="accounts")
router.register(r"workplaces", WorkPlaceView, basename="workplaces")

urlpatterns = [
    path("token/", ExpandedTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("", include(router.urls)),
]

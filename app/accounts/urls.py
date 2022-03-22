from django.urls import path, include

from .views import UserProfileListCreateView, UserProfileDetailView, EmailViewSet, UserProfileViewSet

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("email", EmailViewSet)
router.register("profile", UserProfileViewSet)

urlpatterns = [
    # gets all user profiles and create a new profile
    path("all-profiles", UserProfileListCreateView.as_view(), name="all-profiles"),
    # retrieves profile details of the currently logged in user
    path("profile/<int:pk>", UserProfileDetailView.as_view(), name="profile"),
    path('', include(router.urls))
]

from drf_spectacular.utils import extend_schema
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from src.apps.accounts.mixins import PermissionPerActionMixin, UserViewMixin
from src.apps.accounts.models import User, WorkPlace
from src.apps.accounts.permissions import IsProfileOwner
from src.apps.accounts.serializers import (
    ExpandedTokenObtainPairSerializer,
    RegisterUserSerializer,
    UserProfileSerializer,
    WorkPlaceSerializer,
)


class RegisterViewSet(viewsets.GenericViewSet):
    permission_classes = (AllowAny,)

    @action(
        detail=False,
        methods=["post"],
        url_path="register",
        serializer_class=RegisterUserSerializer,
    )
    def register(self, args, *kwargs):
        """Register new user"""
        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserProfileViewSet(
    UserViewMixin,
    PermissionPerActionMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = UserProfileSerializer
    permission_classes = (AllowAny,)
    permission_classes_by_action = {
        "update": (IsProfileOwner,),
        "partial_update": (IsProfileOwner,),
    }

    def get_queryset(self):
        if self.action in ["partial_update", "update"]:
            return User.objects.all()
        else:
            return User.objects.filter(
                place_of_work__isnull=False,
                position__isnull=False,
                academic_status__isnull=False,
                scientific_degree__isnull=False,
            ).all()


class WorkPlaceView(viewsets.ReadOnlyModelViewSet):
    """ Retrieve list of workplaces with users or singe workplace object """

    queryset = WorkPlace.objects.prefetch_related("employees")
    permission_classes = (AllowAny,)
    serializer_class = WorkPlaceSerializer


class ExpandedTokenObtainPairView(TokenObtainPairView):
    serializer_class = ExpandedTokenObtainPairSerializer

    @extend_schema(
        request=ExpandedTokenObtainPairSerializer,
        responses={
            status.HTTP_200_OK: TokenObtainPairSerializer,
        },
    )
    def post(self, request, *args, **kwargs):
        return super(ExpandedTokenObtainPairView, self).post(request, *args, **kwargs)

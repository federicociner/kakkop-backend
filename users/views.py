from dj_rest_auth.views import LoginView
from dj_rest_auth.registration.views import RegisterView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.settings import api_settings

from users.models import CustomUser
from users.serializers import UserSerializer


class LoginView(LoginView):
    def get_response(self):
        response = super().get_response()
        response.data.update(create_jwt_token_data(response))

        return response


class RegisterView(RegisterView):
    def create(self, request):
        response = super().create(request)
        response.data.update(create_jwt_token_data(response))

        return response


class UserList(ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        first_name = serializer.data["first_name"]
        last_name = serializer.data["last_name"]
        content = {
            "message": f"User '{first_name} {last_name}' successfully deleted."
        }
        super().destroy(request, *args, **kwargs)

        return Response(content, status=status.HTTP_200_OK)


def create_jwt_token_data(response):
    access_expire = int(api_settings.ACCESS_TOKEN_LIFETIME.total_seconds())
    refresh_expire = int(api_settings.REFRESH_TOKEN_LIFETIME.total_seconds())

    return {
        "access_token": {
            "expiration": access_expire,
            "value": response.data["access_token"],
        },
        "refresh_token": {
            "expiration": refresh_expire,
            "value": response.data["refresh_token"],
        },
    }

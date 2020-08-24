from django.urls import path

from users.views import UserDetail, UserList

urlpatterns = [
    path("users/", UserList.as_view()),
    path("users/<int:pk>", UserDetail.as_view()),
]

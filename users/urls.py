from django.urls import path

from .views import UserDetail, UserList

urlpatterns = [
    path("", UserList.as_view(), name="user_list"),
    path("<int:pk>/", UserDetail.as_view(), name="user_detail"),
]

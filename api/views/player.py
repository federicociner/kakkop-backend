from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from ..models.player import Player
from ..serializers.player import PlayerSerializer


class PlayerListApi(ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class PlayerDetailApi(RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def destroy(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        player_id = serializer.data["id"]
        content = {"message": f"Player ID '{player_id}' successfully deleted."}
        super().destroy(request, *args, **kwargs)

        return Response(content, status=status.HTTP_200_OK)

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.response import Response

from ..models.game import Game
from ..serializers.game import GameSerializer


class GameListApi(ListCreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetailApi(RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def destroy(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        game_id = serializer.data["id"]
        content = {"message": f"Game ID '{game_id}' successfully deleted."}
        super().destroy(request, *args, **kwargs)

        return Response(content, status=status.HTTP_200_OK)

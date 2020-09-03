from rest_framework import generics, status
from rest_framework.response import Response

from .models import Game
from .serializers import GameSerializer


class GameApi(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


class GameDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def destroy(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        game_id = serializer.data["id"]
        content = {"message": f"Game ID '{game_id}' successfully deleted."}
        super().destroy(request, *args, **kwargs)

        return Response(content, status=status.HTTP_200_OK)

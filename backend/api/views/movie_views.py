import json

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import permissions, status, generics
from ..models import Movie
from ..serializers import MovieSerializer
from rest_framework.response import Response


class MovieList(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [AllowAny]


class MovieListAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, movie_id):
        movie = Movie.objects.get(id=movie_id)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)


@api_view(['GET'])
@permission_classes((AllowAny, ))
def get_movie_by_genres(request):
    genre_list = json.loads(request.GET['genre_list'])
    movies = Movie.genre_manager.genre_filter(genre_list)
    serializer = MovieSerializer(movies, many=True)
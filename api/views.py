from rest_framework import generics
from .models import Actor, Director, Movie, MovieDirection, MovieCast, Reviewer, Genre, MovieGenre, Rating
from .serializers import ActorSerializer, DirectorSerializer, MovieSerializer, MovieDirectionSerializer, MovieCastSerializer, ReviewerSerializer, GenreSerializer, MovieGenreSerializer, RatingSerializer

class ActorListAPIView(generics.ListAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorCreateAPIView(generics.CreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class ActorUpdateAPIView(generics.UpdateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class DirectorListAPIView(generics.ListAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorCreateAPIView(generics.CreateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class DirectorUpdateAPIView(generics.UpdateAPIView):
    queryset = Director.objects.all()
    serializer_class = DirectorSerializer

class MovieListAPIView(generics.ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieCreateAPIView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieUpdateAPIView(generics.UpdateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDirectionListAPIView(generics.ListAPIView):
    queryset = MovieDirection.objects.all()
    serializer_class = MovieDirectionSerializer

class MovieDirectionCreateAPIView(generics.CreateAPIView):
    queryset = MovieDirection.objects.all()
    serializer_class = MovieDirectionSerializer

class MovieDirectionDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieDirection.objects.all()
    serializer_class = MovieDirectionSerializer

class MovieDirectionUpdateAPIView(generics.UpdateAPIView):
    queryset = MovieDirection.objects.all()
    serializer_class = MovieDirectionSerializer

class MovieCastListAPIView(generics.ListAPIView):
    queryset = MovieCast.objects.all()
    serializer_class = MovieCastSerializer

class MovieCastCreateAPIView(generics.CreateAPIView):
    queryset = MovieCast.objects.all()
    serializer_class = MovieCastSerializer

class MovieCastDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieCast.objects.all()
    serializer_class = MovieCastSerializer

class MovieCastUpdateAPIView(generics.UpdateAPIView):
    queryset = MovieCast.objects.all()
    serializer_class = MovieCastSerializer

class ReviewerListAPIView(generics.ListAPIView):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer

class ReviewerCreateAPIView(generics.CreateAPIView):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer

class ReviewerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer

class ReviewerUpdateAPIView(generics.UpdateAPIView):
    queryset = Reviewer.objects.all()
    serializer_class = ReviewerSerializer

class GenreListAPIView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreCreateAPIView(generics.CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreUpdateAPIView(generics.UpdateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class MovieGenreListAPIView(generics.ListAPIView):
    queryset = MovieGenre.objects.all()
    serializer_class = MovieGenreSerializer

class MovieGenreCreateAPIView(generics.CreateAPIView):
    queryset = MovieGenre.objects.all()
    serializer_class = MovieGenreSerializer

class MovieGenreDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MovieGenre.objects.all()
    serializer_class = MovieGenreSerializer

class MovieGenreUpdateAPIView(generics.UpdateAPIView):
    queryset = MovieGenre.objects.all()
    serializer_class = MovieGenreSerializer

class RatingListAPIView(generics.ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class RatingCreateAPIView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class RatingDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

class RatingUpdateAPIView(generics.UpdateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer

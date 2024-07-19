from django.urls import path
from .views import (
    ActorListAPIView, ActorCreateAPIView, ActorDetailAPIView, ActorUpdateAPIView,
    DirectorListAPIView, DirectorCreateAPIView, DirectorDetailAPIView, DirectorUpdateAPIView,
    MovieListAPIView, MovieCreateAPIView, MovieDetailAPIView, MovieUpdateAPIView,
    MovieDirectionListAPIView, MovieDirectionCreateAPIView, MovieDirectionDetailAPIView, MovieDirectionUpdateAPIView,
    MovieCastListAPIView, MovieCastCreateAPIView, MovieCastDetailAPIView, MovieCastUpdateAPIView,
    ReviewerListAPIView, ReviewerCreateAPIView, ReviewerDetailAPIView, ReviewerUpdateAPIView,
    GenreListAPIView, GenreCreateAPIView, GenreDetailAPIView, GenreUpdateAPIView,
    MovieGenreListAPIView, MovieGenreCreateAPIView, MovieGenreDetailAPIView, MovieGenreUpdateAPIView,
    RatingListAPIView, RatingCreateAPIView, RatingDetailAPIView, RatingUpdateAPIView
)

urlpatterns = [
    path('actors/', ActorListAPIView.as_view(), name='actor-list'),
    path('actors/create/', ActorCreateAPIView.as_view(), name='actor-create'),
    path('actors/<int:pk>/', ActorDetailAPIView.as_view(), name='actor-detail'),
    path('actors/<int:pk>/update/', ActorUpdateAPIView.as_view(), name='actor-update'),

    path('directors/', DirectorListAPIView.as_view(), name='director-list'),
    path('directors/create/', DirectorCreateAPIView.as_view(), name='director-create'),
    path('directors/<int:pk>/', DirectorDetailAPIView.as_view(), name='director-detail'),
    path('directors/<int:pk>/update/', DirectorUpdateAPIView.as_view(), name='director-update'),

    path('movies/', MovieListAPIView.as_view(), name='movie-list'),
    path('movies/create/', MovieCreateAPIView.as_view(), name='movie-create'),
    path('movies/<int:pk>/', MovieDetailAPIView.as_view(), name='movie-detail'),
    path('movies/<int:pk>/update/', MovieUpdateAPIView.as_view(), name='movie-update'),

    path('movie-directions/', MovieDirectionListAPIView.as_view(), name='movie-direction-list'),
    path('movie-directions/create/', MovieDirectionCreateAPIView.as_view(), name='movie-direction-create'),
    path('movie-directions/<int:pk>/', MovieDirectionDetailAPIView.as_view(), name='movie-direction-detail'),
    path('movie-directions/<int:pk>/update/', MovieDirectionUpdateAPIView.as_view(), name='movie-direction-update'),

    path('movie-casts/', MovieCastListAPIView.as_view(), name='movie-cast-list'),
    path('movie-casts/create/', MovieCastCreateAPIView.as_view(), name='movie-cast-create'),
    path('movie-casts/<int:pk>/', MovieCastDetailAPIView.as_view(), name='movie-cast-detail'),
    path('movie-casts/<int:pk>/update/', MovieCastUpdateAPIView.as_view(), name='movie-cast-update'),
    path('reviewers/', ReviewerListAPIView.as_view(), name='reviewer-list'),
    path('reviewers/create/', ReviewerCreateAPIView.as_view(), name='reviewer-create'),
    path('reviewers/<int:pk>/', ReviewerDetailAPIView.as_view(), name='reviewer-detail'),
    path('reviewers/<int:pk>/update/', ReviewerUpdateAPIView.as_view(), name='reviewer-update'),
    path('genres/', GenreListAPIView.as_view(), name='genre-list'),
    path('genres/create/', GenreCreateAPIView.as_view(), name='genre-create'),
    path('genres/<int:pk>/', GenreDetailAPIView.as_view(), name='genre-detail'),
    path('genres/<int:pk>/update/', GenreUpdateAPIView.as_view(), name='genre-update'),

    path('movie-genres/', MovieGenreListAPIView.as_view(), name='movie-genre-list'),
    path('movie-genres/create/', MovieGenreCreateAPIView.as_view(), name='movie-genre-create'),
    path('movie-genres/<int:pk>/', MovieGenreDetailAPIView.as_view(), name='movie-genre-detail'),
    path('movie-genres/<int:pk>/update/', MovieGenreUpdateAPIView.as_view(), name='movie-genre-update'),

    path('ratings/', RatingListAPIView.as_view(), name='rating-list'),
    path('ratings/create/', RatingCreateAPIView.as_view(), name='rating-create'),
    path('ratings/<int:pk>/', RatingDetailAPIView.as_view(), name='rating-detail'),
    path('ratings/<int:pk>/update/', RatingUpdateAPIView.as_view(), name='rating-update'),
]

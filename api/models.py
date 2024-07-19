from django.db import models

class Actor(models.Model):
    act_id = models.AutoField(primary_key=True)
    act_fname = models.CharField(max_length=100)
    act_lname = models.CharField(max_length=100)
    act_gender = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.act_fname} {self.act_lname}"


class Director(models.Model):
    dir_id = models.AutoField(primary_key=True)
    dir_fname = models.CharField(max_length=200)
    dir_lname = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.dir_fname} {self.dir_lname}"


class Movie(models.Model):
    movie_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    movie_land = models.CharField(max_length=255)
    mov_rel_country = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class MovieDirection(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie.title} directed by {self.director.dir_fname} {self.director.dir_lname}"


class MovieCast(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)
    role = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.actor.act_fname} {self.actor.act_lname} as {self.role} in {self.movie.title}"


class Reviewer(models.Model):
    rev_id = models.AutoField(primary_key=True)
    rev_name = models.CharField(max_length=255)

    def __str__(self):
        return self.rev_name


class Genre(models.Model):
    genre_id = models.AutoField(primary_key=True)
    genre_name = models.CharField(max_length=100)

    def __str__(self):
        return self.genre_name


class MovieGenre(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.movie.title} in {self.genre.genre_name}"


class Rating(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    reviewer = models.ForeignKey(Reviewer, on_delete=models.CASCADE)
    rating = models.IntegerField()
    numo_ratings = models.IntegerField()

    def __str__(self):
        return f"{self.movie.title} rated {self.rating} by {self.reviewer.rev_name}"

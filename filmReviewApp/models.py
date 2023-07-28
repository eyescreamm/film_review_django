from django.db import models

# Create your models here.

class Film(models.Model):
    title = models.CharField(max_length=100)
    count_reviews = models.IntegerField()
    
    def __str__(self):
        return self.title

class User(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    film = models.ForeignKey(Film, on_delete=models.PROTECT)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.user.name) + " " + str(self.created_at)

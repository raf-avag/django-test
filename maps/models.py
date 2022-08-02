from django.db import models
from datetime import date


# class Country(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return str(self.name)


# # The model Capital
# class Capital(models.Model):
#     country = models.OneToOneField(
#         Country,
#         on_delete=models.CASCADE,
#         primary_key=True,
#     )

#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return str(self.name)

# The model City
class Subject(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return str(self.title)


class University(models.Model):
    name = models.CharField(max_length=100)
    subject = models.ManyToManyField(Subject)
    pic = models.ImageField()

    def __str__(self):
        return self.name

    def natural_key(self):
        return self.name


# class Author(models.Model):
#     name = models.CharField(max_length=200)
#     email = models.EmailField()

#     def __str__(self):
#         return self.name


# class Entry(models.Model):
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
#     headline = models.CharField(max_length=255)
#     body_text = models.TextField()
#     pub_date = models.DateField()
#     mod_date = models.DateField(default=date.today)
#     authors = models.ManyToManyField(Author)
#     number_of_comments = models.IntegerField(default=0)
#     number_of_pingbacks = models.IntegerField(default=0)
#     rating = models.IntegerField(default=5)

#     def __str__(self):
#         return self.headline
from django.db import models
from django.urls import reverse



# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False)
    text = models.TextField()
    upcoming = models.BooleanField()
    # image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)


    class Meta:
        verbose_name = ("Post")
        verbose_name_plural = ("Posts")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ventureapp:post_detail", kwargs={"pk": self.pk})


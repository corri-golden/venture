from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User



# Create your models here.



class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    date = models.DateField(auto_now=False, auto_now_add=False)
    text = models.TextField()
    upcoming = models.BooleanField()
    # images is create automatically
    post_image = models.ImageField(null=True, blank=True, upload_to="images/")
    likes = models.ManyToManyField(User, related_name='blog_post')
    

    def total_likes(self):
        return self.likes.count()
    
    def publish(self):
        self.save()

    # class Meta:
    #     verbose_name = ("Post")
    #     verbose_name_plural = ("Posts")

    def __str__(self):
        return self.location

    #this can be used for redirect.
    def get_absolute_url(self):
        return reverse("ventureapp:post_list")


class Comment(models.Model):
    # allows us to reference this model as comments on blog post page
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    body = models.TextField()

    #test
    # author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #test


    # add the date to the post so the person won't have to type it
    date_added = models.DateField(auto_now_add=True)

    # for this model to show up easily and readable in django admin
    def __str__(self):
        # on admin this will show the post title that we are comment on and the person name.
        return '%s - %s' % (self.post.location, self.name)

    


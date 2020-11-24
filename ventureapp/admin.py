from django.contrib import admin
from ventureapp.models import Post, Comment

# Register your models here.
# So there will show up in the django admin area
admin.site.register(Post)
admin.site.register(Comment)
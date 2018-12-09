from django.contrib import admin
from rest.models import Snippet,User,Post,Comment
# Register your models here.
admin.site.register(Snippet)
admin.site.register(User)
admin.site.register(Post)
admin.site.register(Comment)

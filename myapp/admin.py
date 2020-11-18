from django.contrib import admin

# Register your models here.
from .models import Post

# fazendo esse registro ele faz com que apareça na area administrativa
admin.site.register(Post)
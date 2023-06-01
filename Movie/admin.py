from django.contrib import admin
from Movie.models import Movie

# Register your models here.


class MovieAdmin(admin.ModelAdmin):
    list_display=['rdate','movieName','hero','heroine','rating']
admin.site.register(Movie,MovieAdmin)

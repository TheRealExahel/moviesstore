from django.contrib import admin

# Register your models here.
from .models import Movie, Review
class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']
admin.site.register(Movie, MovieAdmin)
admin.site.register(Review)

class ReviewAdmin(admin.ModelAdmin):
    search_fields = ("comment", "reason")
    list_filter = ("reported")
    list_display = ("id", "user", "reported", "reason")
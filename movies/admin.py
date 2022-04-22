from django.contrib import admin
from .models import Actor,Movie,Review
# Register your models here.

class ActorAdmin(admin.ModelAdmin) :

    model = Actor
    list_display = ('name',)


class MovieAdmin(admin.ModelAdmin) :

    model = Movie
    list_display = ('title','overview',)


class ReviewAdmin(admin.ModelAdmin) :

    model = Actor
    list_display = ('title','content')

admin.site.register(Actor,ActorAdmin)
admin.site.register(Movie,MovieAdmin)
admin.site.register(Review,ReviewAdmin)
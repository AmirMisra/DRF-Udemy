from django.http import JsonResponse

from .models import Movies


# Create your views here.

def movie_list(request):
    movies = Movies.objects.all()
    # print(movies.values())
    data = {
        'movies': list(movies.values())
    }
    return JsonResponse(data)

from django.http.response import JsonResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    msg = "Hello There!"
    context = {
      "msg": msg 
    }
    return render(request, 'index.html', context)

def people(request):
    people = [
        {'name': 'Mark', 'image': 'https://via.placeholder.com/150'},
        {'name': 'Jeff', 'image': 'https://via.placeholder.com/150'},
    ]

    return JsonResponse(people, safe=False)

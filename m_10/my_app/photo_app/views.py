from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'photo_app/index.html', context={'title': 'Main Page'})
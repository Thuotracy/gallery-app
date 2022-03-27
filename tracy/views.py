from django.shortcuts import render,redirect
from django.http  import HttpResponse
from .models import Image,Location,categories

# Create your views here.
def gallery(request):
    images = Image.all_images()
    locations = Location.objects.all()
    return render(request, 'pictures/index.html', {"images":images,"locations":locations})

def location(request,location):
    locations = Location.objects.all()
    selected_location = Location.objects.get(id = location)
    images = Image.objects.filter(locations = selected_location.id)
    return render(request, 'pictures/location.html', {"location":selected_location,"locations":locations,"images":images})


def search(request):
    if 'imagesearch' in request.GET and request.GET["imagesearch"]:
        search_term = request.GET.get("category")
        category = request.GET.get("imagesearch")
        searched_images = Image.search_by_category(category)
        message = f"{category}"
        print(searched_images)
        return render(request,'pictures/search.html',{"images":searched_images,"category":search_term})
    else:
        message = "You haven't searched for any image category"
        return render(request, 'pictures/search.html', {"message": message})
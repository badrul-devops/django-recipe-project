from django.shortcuts import render,redirect
from recipe_app.models import *



# Create your views here.
def recipes(request):
    if request.method == "POST":
        data= request.POST
        name= data.get('name')
        ingredients= data.get('ingredients')
        time_required= data.get('time_required')
        description= data.get('description')
        image = request.FILES.get('image')
        
        Recipe.objects.create(name=name, 
            ingredients=ingredients, 
            time_required=time_required,
            description=description,
            image=image,)
        return redirect('/')
        
    return render(request, 'recipes.html')

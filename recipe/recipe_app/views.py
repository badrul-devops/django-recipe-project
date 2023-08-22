from django.shortcuts import render,redirect
from recipe_app.models import Recipe

from django.contrib.auth.models import User



# Create your views here.

def recipes(request):
    if request.method == "POST":
        
        data= request.POST
        name= data.get('name')
        ingredients= data.get('ingredients')
        
        description= data.get('description')
        image = request.FILES.get('image')
        # pylint: disable=no-member

        
        Recipe.objects.create(name=name,
            ingredients=ingredients,
            description=description,
            image=image,)
        return redirect('/')
    
    # pylint: disable=no-member
    query = Recipe.objects.all()
    if request.GET.get('search'):
        query = query.filter(name__icontains=request.GET.get('search'))
        
    
    
    context = {'recipes': query }
        
    return render(request, 'recipes.html', context)

def delete_recipes(request,id ):
    # pylint: disable=no-member
    queary= Recipe.objects.get(id = id)
    queary.delete()
    return redirect('/')


def login_page(request):
    return render(request, 'loginpage.html')

def register_page(request):
    if request.method == 'POST':
        data= request.POST
        fast_name= data.get('fast_name')
        last_name= data.get('last_name')
        username= data.get('user_name')
        email= data.get('email')
        password= data.get('password')
        
        # pylint: disable=no-member
        user = User.objects.create(firstname=fast_name,lastname=last_name, email=email , username=username)
        user.set_password(password)
    
        user.save()
    return render(request,'register.html')
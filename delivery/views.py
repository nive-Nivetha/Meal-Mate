from django.shortcuts import render,get_object_or_404, redirect
from django.http import HttpResponse
from delivery.models import Customer,Restaurant,MenuItem


def index(request):
    return render(request,'delivery/index.html')

def signin(request):
    return render(request,'delivery/signin.html')

def signup(request):
    return render(request,'delivery/signup.html')

def handle_signin(request):
    
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password') 

        try:
            cust = Customer.objects.get(username=username,password=password)
            if username == 'admin':
                return render(request,'delivery/success.html',{"c":cust})
            else:
                restaurants = Restaurant.objects.all()
                return render(request,'delivery/customer_home.html',{"c":cust,"restaurants":restaurants})
        except:
            return render(request,'delivery/error.html')
        
    else:
        return HttpResponse("Invalid request")
    
def handle_signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        number = request.POST.get('number')

        try:
            # already exists
            cust = Customer.objects.get(username=username,password=password)
            return HttpResponse("username already exists.Please use other username for signup..")
        except:
            c = Customer(username =username ,password=password,email=email,number=number)
            c.save()

        return render(request,'delivery/signin.html')
    else:
        return HttpResponse("Invalid request")
    
def restaurant_page(request):
    return render(request,"delivery/addrestraunt.html")


def add_restaurant(request):
    if request.method == "POST":
        resname = request.POST.get('resname')
        resimage = request.POST.get('resimage')
        cuisine = request.POST.get('cuisine')
        rating = request.POST.get('rating')
        
        res=Restaurant(resname=resname,resimage=resimage,cuisine=cuisine,rating=rating)
        res.save()

        restaurants = Restaurant.objects.all()

        return render(request,'delivery/show_restaurants.html',{"restaurants":restaurants})
    else:
        return HttpResponse("Invalid request")
    
def show_restaurant_page(request):
    restaurants=Restaurant.objects.all()
    return render(request,'delivery/show_restaurants.html',{"restaurants":restaurants})

def restaurant_menu(request,restaurant_id):
    restaurant=get_object_or_404(Restaurant,id=restaurant_id)
    if request.method=="POST":
        name = request.POST.get('name')
        description = request.POST.get('description')
        price = request.POST.get('price')
        picture = request.POST.get('picture')
        isVeg=request.POST.get('is_veg')=='on'

        MenuItem.objects.create(restaurant=restaurant,name=name,description=description,price=price,picture=picture,isVeg=isVeg)

        return redirect('restaurant_menu',restaurant_id=restaurant_id)
    
    menu_items=restaurant.menu_items.all()
    return render(request,'delivery/menu.html',{
        'restaurant':restaurant,
        'menu_items':menu_items,
    })

def update_restaurant_page(request,restaurant_id):
    restaurant = get_object_or_404(Restaurant,id=restaurant_id)
    return render(request,'delivery/update_restaurant_page.html',{"restaurant":restaurant})

def update_restaurant(request,restaurant_id):
    restaurant = get_object_or_404(Restaurant,id=restaurant_id)
    if request.method == "POST":
        restaurant.resname = request.POST.get('name')
        restaurant.resimage = request.POST.get('picture')
        restaurant.cuisine = request.POST.get('cuisine')
        restaurant.rating = request.POST.get('rating')
        restaurant.save()
        
        return redirect('show_restaurant_page')  

    return render(request, 'delivery/update_restaurant_page.html', {'restaurant': restaurant})
    
def delete_restaurant(request,restaurant_id):
    restaurant = get_object_or_404(Restaurant,id=restaurant_id)
    if request.method == 'POST':
       restaurant.delete()
       return redirect('show_restaurant_page')
    return redirect('restaurant_menu', restaurant_id=restaurant_id)

def update_menuItem_page(request,menuItem_id):
    MenuItem = get_object_or_404(MenuItem,id=menuItem_id)
    return render(request,'delivery/update_menuItem_page.html',{"menuItem":MenuItem})

def update_menuItem(request,menuItem_id):
    Menu_item = get_object_or_404(MenuItem,id=menuItem_id)
    restaurant = Menu_item.restaurant
    if request.method == "POST":
        Menu_item.name = request.POST.get('name')
        Menu_item.picture = request.POST.get('picture')
        Menu_item.price = request.POST.get('price')
        Menu_item.isVeg = request.POST.get('isVeg') =='on'
        Menu_item.description = request.POST.get('description')
        Menu_item.save()
        
        return redirect('restaurant_menu',restaurant.id)  

    return render(request, 'delivery/update_menuItem_page.html', {'menuItem': Menu_item})
    
def delete_menuItem(request, menuItem_id):
    Menu_item = get_object_or_404(MenuItem, id=menuItem_id)
    restaurant = Menu_item.restaurant
    restaurant_id = restaurant.id  

    if request.method == 'POST':
        Menu_item.delete()
        return redirect('restaurant_menu', restaurant_id=restaurant_id)

    return redirect('restaurant_menu', restaurant_id=restaurant_id)

def customer_menu(request,restaurant_id):
    restaurant=get_object_or_404(Restaurant,id=restaurant_id)
    menu_items=restaurant.menu_items.all()

    return render(request,'delivery/customer_menu.html',{
        'restaurant':restaurant,
        'menu_items':menu_items,
    })

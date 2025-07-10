from django.shortcuts import render
from django.http import HttpResponse
from delivery.models import Customer,Restaurant

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
            return render(request,'delivery/success.html',{"c":cust})
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
    

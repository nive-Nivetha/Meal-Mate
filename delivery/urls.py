from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('signin/',views.signin),
    path('signup/',views.signup),
    path('handle_signin/',views.handle_signin,name='handle_signin'),
    path('handle_signup/',views.handle_signup,name='handle_signup'),
    path('handle_signin/restaurant_page/',views.restaurant_page,name='restaurant_page'),
    path('handle_signin/add_restaurant/',views.add_restaurant,name='add_restaurant'),
]

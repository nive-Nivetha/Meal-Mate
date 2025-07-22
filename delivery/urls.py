from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('signin/',views.signin),
    path('signup/',views.signup),
    path('handle_signin/',views.handle_signin,name='handle_signin'),
    path('handle_signup/',views.handle_signup,name='handle_signup'),
    
    path('handle_signin/show_restaurant_page/',views.show_restaurant_page,name='show_restaurant_page'),
    path('handle_signin/add_restaurant/',views.add_restaurant,name='add_restaurant'),
    path('handle_signin/<int:restaurant_id>/',views.restaurant_page,name='restaurant_page'),
    path('restaurant/<int:restaurant_id>/menu/',views.restaurant_menu,name='restaurant_menu'),
    path('restaurant/<int:restaurant_id>/update/', views.update_restaurant, name='update_restaurant'),
    path('restaurant/<int:restaurant_id>/update/page/', views.update_restaurant_page, name='update_restaurant_page'),
    path('restaurant/<int:restaurant_id>/delete/', views.delete_restaurant, name='delete_restaurant'),

    path('menu/<int:menuItem_id>/update/', views.update_menuItem, name='update_menuItem'),
    path('menu/<int:menuItem_id>/update/page/', views.update_menuItem_page, name='update_menuItem_page'),
    path('menu/<int:menuItem_id>/delete/', views.delete_menuItem, name='delete_menuItem'),

    path('restaurant/<int:restaurant_id>/menu/customer/',views.customer_menu,name='customer_menu'),

]

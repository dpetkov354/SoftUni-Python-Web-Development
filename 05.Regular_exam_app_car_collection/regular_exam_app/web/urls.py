from django.urls import path
from regular_exam_app.web.views import show_home, car_create, car_details, car_edit, car_delete, profile_details, \
    profile_delete, create_profile, edit_profile, catalogue

urlpatterns = (
     path('', show_home, name='show home'),

     path('catalogue/', catalogue, name='catalogue'),
     path('car/create/', car_create, name='car create'),
     path('car/details/<int:pk>/', car_details, name='car details'),
     path('car/edit/<int:pk>/', car_edit, name='car edit'),
     path('car/delete/<int:pk>/', car_delete, name='car delete'),

     path('profile/create/', create_profile, name='create profile'),
     path('profile/edit/', edit_profile, name='edit profile'),
     path('profile/details/', profile_details, name='profile details'),
     path('profile/delete/', profile_delete, name='profile delete'),
     )

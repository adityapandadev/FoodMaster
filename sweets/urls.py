from django.urls import path
from django.urls.conf import include
from sweets import views
from django.views.generic.base import RedirectView
urlpatterns = [ 
    path('home/', views.HomeView.as_view()),
    path('sweetshop/', views.SweetshopListView.as_view()),
    path('sweetshop/<int:pk>', views.SweetshopDetailView.as_view()),
    path('', RedirectView.as_view(url="home/")),  
    path('contact/submit', views.contact),
     
   
]

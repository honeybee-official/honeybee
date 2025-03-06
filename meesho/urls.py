from django.urls import path
from meesho.views import contact_success_view, contact_view, home, about, contact, category , register , login , success

urlpatterns = [

    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('category/', category, name='category'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('success/', success, name='success'),
    path('contact-me/', contact_view, name='contact-me'),
    path('contact-me/success', contact_success_view, name='contact-success'),   
]

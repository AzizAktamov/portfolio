from django.urls import path
from .views import home_view,about_view,do_view,portfolio_view,contact_view

urlpatterns = [
    path('',home_view,name='home-page'),
    path('about/',about_view,name='about-page'),
    path('do/',do_view,name='do-page'),
    path('portfolio/',portfolio_view,name='portfolio-page'),
    path('contact/',contact_view,name='contact-page'),
]
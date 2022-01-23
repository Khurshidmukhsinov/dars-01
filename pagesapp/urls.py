from django.urls import path
from .views import HomePageView,AboutPageView,ServPageView

urlpatterns = [
    path('serv/', ServPageView.as_view(), name='serv'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home')
]
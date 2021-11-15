from django.urls import path
from .views import (
    HomePageView, 
    AboutUsPageView
    )


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about_us", AboutUsPageView.as_view(), name="about_us"),
]

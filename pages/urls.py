from django.urls import path

from .views import HomePageView, AboutPageView , ContactPageView, ServicesPageView, ClientPageView , home_page_view

urlpatterns = [
    # path("", HomePageView.as_view(), name="home"),
    path("", home_page_view , name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("services/", ServicesPageView.as_view(), name="services"),
    path("clients/", ClientPageView.as_view(), name="clients"),
]


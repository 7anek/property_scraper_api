from django.urls import path
from properties import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('login/', auth_views.LoginView.as_view(template_name="properties/login.html"), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path("search/", views.search, name="search"),
    path("scrape/", views.scrape, name="scrape"),
    # path("scrape/<uuid:scrape_job_id>", views.get_scrape, name="get_scrape")
    path("scrape/<str:uuids>", views.get_scrape, name="get_scrape")
]
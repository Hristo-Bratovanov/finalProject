from django.urls import path

from finalProject.common import views

urlpatterns = [
    path('',views.HomePage.as_view(), name='home'),
    path('nav/', views.NavPage.as_view(), name='nav'),
]
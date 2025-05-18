from django.urls import path
from finalProject.common import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('like/<int:project_id>/', views.likes_functionality, name='like'),
    path('share/<int:project_id>/', views.share_functionality, name='share'),
    path('comment/<int:project_id>/', views.comment_functionality, name='comment'),
]
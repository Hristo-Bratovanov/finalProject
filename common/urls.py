from django.urls import path
from common import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('share/<int:photo_id>/', views.share_functionality, name='share'),
    path('comment/<int:photo_id>/', views.comment_functionality, name='comment'),
    path('companies/', views.CompanyList.as_view(), name='companies'),
]
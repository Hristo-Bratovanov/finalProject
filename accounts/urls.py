from django.urls import path, include

from accounts import views

urlpatterns = [
    path('register/', views.AppUserRegisterView.as_view(), name='register'),
    path('login/', views.AppUserLoginView.as_view(), name='login'),
    path('logout/', views.AppUserLogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/', include([
        path('', views.ProfileDetailsView.as_view(), name='company-details'),
        path('edit/', views.ProfileEditView.as_view(), name='company-edit'),
        path('delete/', views.ProfileDeleteView.as_view(), name='company-delete'),
    ]))
]
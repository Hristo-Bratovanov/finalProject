from django.urls import path, include

from finalProject.professionals import views

urlpatterns = [
    path('add/', views.ProfessionalAddPage.as_view(), name='add-professional'),
    path('<str:username>/professional/<slug:professional_slug>', include([
        path('', views.ProfessionalDetailsPage.as_view(), name='professional-details'),
        path('edit/', views.ProfessionalEditPage.as_view(), name='professional-edit'),
        path('delete/', views.ProfessionalDeletePage.as_view(), name='professional-delete'),
    ]))
]
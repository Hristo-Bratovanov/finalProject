from django.urls import path, include

from finalProject.projects import views

urlpatterns = [
    path('add/', views.ProjectAddView.as_view(), name='project-add'),
    path('<int:pk>/', include([
        path('', views.ProjectDetailsView.as_view(), name='project-details'),
        path('edit/', views.ProjectEditView.as_view(), name='project-edit'),
        path('delete/', views.project_delete, name='project-delete'),
    ])),
]
from django.urls import path, include

from finalProject.projects import views

urlpatterns = [
    path('add/', views.ProjectAddView.as_view(), name='add-project'),
    path('<str:username>/project/<slug:project_slug>', include([
        path('', views.ProjectDetailsView.as_view(), name='project-details'),
        path('edit/', views.ProjectEditView.as_view(), name='project-edit'),
        path('delete/', views.ProjectDeleteView.as_view(), name='project-delete'),
    ]))
]
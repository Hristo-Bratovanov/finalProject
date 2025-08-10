from django.urls import path, include

from project_pictures import views

urlpatterns = [
    path('add/', views.PictureAddView.as_view(), name='picture-add'),
    path('<int:pk>/', include([
        path('', views.PictureDetailsView.as_view(), name='picture-details'),
        path('edit/', views.PictureEditView.as_view(), name='picture-edit'),
        path('delete/', views.picture_delete, name='picture-delete'),
    ])),
]
from django.urls import path, include

from employees import views

urlpatterns = [
    path('add/', views.EmployeeAddView.as_view(), name='employee-add'),
    path('<int:pk>/', include([
        path('', views.EmployeeDetailsView.as_view(), name='employee-details'),
        path('edit/', views.EmployeeEditView.as_view(), name='employee-edit'),
        path('delete/', views.EmployeeDeleteView.as_view(), name='employee-delete'),
    ]))
]
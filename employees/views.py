from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from common.mixins import NeverCacheMixin
from employees.forms import EmployeeAddForm, EmployeeEditForm
from employees.models import Employee
from projects.models import Project


class EmployeeAddView(NeverCacheMixin, LoginRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeAddForm
    template_name = 'employees/employee-add-page.html'

    def get_success_url(self):
        return reverse_lazy(
            'company-details',
            kwargs={
                'pk': self.request.user.pk
            }
        )

    def form_valid(self, form):
        employee = form.save(commit=False)
        employee.user = self.request.user
        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['projects'].queryset = Project.objects.filter(user=self.request.user)
        return form


class EmployeeDetailsView(NeverCacheMixin, LoginRequiredMixin, DetailView):
    model = Employee
    template_name = 'employees/employee-details-page.html'


class EmployeeEditView(NeverCacheMixin, LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Employee
    form_class = EmployeeEditForm
    template_name = 'employees/employee-edit-page.html'
    context_object_name = 'employee'

    def test_func(self):
        return self.request.user == self.get_object().user

    def get_success_url(self):
        return reverse_lazy('employee-details', kwargs={'pk': self.get_object().pk})


class EmployeeDeleteView(NeverCacheMixin, LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Employee
    template_name = 'employees/employee-delete-page.html'

    def get_success_url(self):
        return reverse_lazy(
            'company-details',
            kwargs={
                'pk': self.request.user.pk,
            }
        )

    def test_func(self):
        return self.request.user == self.get_object().user

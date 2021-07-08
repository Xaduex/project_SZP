from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django_tables2 import SingleTableView

from SZP.models import Machines, Employee
from django.urls import reverse_lazy

from SZP.permission_mixin import MyTestUserPassesTest


class IndexView(View):
    def get(self, request):
        return render(request, 'base.html')

class MachinesListView(LoginRequiredMixin, SingleTableView):
    model = Machines
    template_name = 'machine_list_view.html'

class CreateMachineView(LoginRequiredMixin, CreateView):
    model = Machines
    template_name = 'form.html'
    fields = ['name', 'vendor', 'serial_number', 'power_consumption', 'type', 'orientation', 'pressure', 'pressure_tank', 'tank']
    success_url = reverse_lazy('machines')


class UpdateMachineView(LoginRequiredMixin, UpdateView):
    model = Machines
    template_name = 'form.html'
    fields = ['name', 'vendor', 'serial_number', 'power_consumption', 'type', 'orientation', 'pressure', 'pressure_tank', 'tank']
    success_url = reverse_lazy('machines')

class DeleteMachineView(LoginRequiredMixin, DeleteView):
    model = Machines
    template_name = 'delete.html'
    success_url = reverse_lazy('machines')

from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from SZP.models import Machines
from django.urls import reverse_lazy


class IndexView(View):
    def get(self, request):
        return render(request, 'base.html')

class MachinesListView(ListView):
    model = Machines
    template_name = 'machine_list_view.html'

class CreateMachineView(CreateView):
    model = Machines
    template_name = 'form.html'
    fields = ['name', 'vendor', 'serial_number', 'power_consumption', 'type', 'orientation', 'pressure', 'pressure_tank', 'tank']
    success_url = reverse_lazy('machines')

class UpdateMachineView(UpdateView):
    model = Machines
    template_name = 'form.html'
    fields = ['name', 'vendor', 'serial_number', 'power_consumption', 'type', 'orientation', 'pressure', 'pressure_tank', 'tank']
    success_url = reverse_lazy('machines')

class DeleteMachineView(DeleteView):
    model = Machines
    template_name = 'delete.html'
    success_url = reverse_lazy('machines')

from typing import Any

from cars.forms import CarForm
from cars.models import Car
from django.contrib.auth.decorators import login_required
from django.db.models.query import QuerySet
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

# class CarsView(View):
    
#     def get (self, request):
#         cars = Car.objects.all().order_by('model')
#         search = request.GET.get('search')

#         if search:
#             cars = Car.objects.filter(model__contains=search)

#         return render(request, 'cars.html', { 'cars': cars })
    
class CarsListView(ListView):
    model = Car
    template_name = 'cars.html'
    context_object_name = 'cars'
    
    def get_queryset(self):
        cars = super().get_queryset().order_by('model')
        #mesma coisa: Car.objects.all().order_by('model')
        #super: acessa coisas da classe pai
        
        search = self.request.GET.get('search')
        if search:
            cars = cars.filter(model__contains=search)
        return cars

# class NewCarView(View):
#     def get (self, request):
#         new_car_form = CarForm()
#         return render(request, 'new_car.html', { 'new_car_form': new_car_form })
    
#     def post(self, request):
#         new_car_form = CarForm(request.POST, request.FILES)
#         if new_car_form.is_valid():
#             new_car_form.save()
#             return redirect('cars_list')
#         return render(request, 'new_car.html', { 'new_car_form': new_car_form })
class CarDetailsView(DetailView):
    model = Car
    template_name = 'car_detail.html'

@method_decorator(login_required(login_url='login'), name='dispatch')
class NewCarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'new_car.html'
    success_url = '/cars/'

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'car_update.html'
    
    def get_success_url(self):
        return reverse_lazy('car_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required(login_url='login'), name='dispatch')
class CarDeleteView(DeleteView):
    model = Car
    template_name= 'car_delete.html'
    success_url = '/cars/'
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Snacks
# Create your views here.


class snacksListView(ListView):
    model= Snacks
    template_name = "snack_list.html"
    context_object_name='snacks'



class SnackDetailView(DetailView):
    model=Snacks 
    template_name='snacks_detail.html'



class snaksCreateView(CreateView):
    model= Snacks
    template_name='snacks_create.html'
    fields=['title_field' ,'purchaser_field','description_field']
    success_url='/'

class snacksUpdateView(UpdateView):
    model=Snacks
    template_name='snacks_update.html'  
    fields=['title_field' ,'purchaser_field','description_field']

class snacksDeleteView(DeleteView):
    model=Snacks
    template_name='snacks_delete.html'  
    success_url= reverse_lazy('snack_list')







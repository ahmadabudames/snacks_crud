from django.urls import path
from django.urls.resolvers import URLPattern

from .views import *

urlpatterns=[
     path('', snacksListView.as_view(), name= 'snack_list'),
     path('<int:pk>/', SnackDetailView.as_view(), name= 'snacks_detail'),
     path('create/', snaksCreateView.as_view(), name= 'snacks_create'),
     path('<int:pk>/update/', snacksUpdateView.as_view(), name= 'snacks_update'),
     path('<int:pk>/delete/', snacksDeleteView.as_view(), name= 'snacks_delete'),


]
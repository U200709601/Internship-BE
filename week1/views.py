from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class GlobalOperatorListView(ModelViewSet):
    queryset = GlobalOperator.objects.all()
    serializer_class = GlobalOperatorSerializer



class GlobalOperatorCreateView(generic.CreateView):
    model = models.GlobalOperator
    form_class = forms.GlobalOperatorForm


class GlobalOperatorDetailView(generic.DetailView):
    model = models.GlobalOperator
    form_class = forms.GlobalOperatorForm


class GlobalOperatorUpdateView(generic.UpdateView):
    model = models.GlobalOperator
    form_class = forms.GlobalOperatorForm
    pk_url_kwarg = "pk"


class GlobalOperatorDeleteView(generic.DeleteView):
    model = models.GlobalOperator
    success_url = reverse_lazy("operator_GlobalOperator_list")



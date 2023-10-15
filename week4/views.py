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



class PortabilityDatabaseListView(ModelViewSet):
    queryset = PortabilityDatabase.objects.all()
    serializer_class = PortabilityDatabaseSerializer


class PortabilityDatabaseCreateView(generic.CreateView):
    model = models.PortabilityDatabase
    form_class = forms.PortabilityDatabaseForm


class PortabilityDatabaseDetailView(generic.DetailView):
    model = models.PortabilityDatabase
    form_class = forms.PortabilityDatabaseForm


class PortabilityDatabaseUpdateView(generic.UpdateView):
    model = models.PortabilityDatabase
    form_class = forms.PortabilityDatabaseForm
    pk_url_kwarg = "pk"


class PortabilityDatabaseDeleteView(generic.DeleteView):
    model = models.PortabilityDatabase
    success_url = reverse_lazy("operator_PortabilityDatabase_list")


class NetworkOperatorListView(ModelViewSet):
    queryset = NetworkOperator.objects.all()
    serializer_class = NetworkOperatorSerializer


class NetworkOperatorCreateView(generic.CreateView):
    model = models.NetworkOperator
    form_class = forms.NetworkOperatorForm


class NetworkOperatorDetailView(generic.DetailView):
    model = models.NetworkOperator
    form_class = forms.NetworkOperatorForm


class NetworkOperatorUpdateView(generic.UpdateView):
    model = models.NetworkOperator
    form_class = forms.NetworkOperatorForm
    pk_url_kwarg = "pk"


class NetworkOperatorDeleteView(generic.DeleteView):
    model = models.NetworkOperator
    success_url = reverse_lazy("operator_NetworkOperator_list")

class LicensedOperatorListView(ModelViewSet):
    queryset = LicensedOperator.objects.all()
    serializer_class = LicensedOperatorSerializer


class LicensedOperatorCreateView(generic.CreateView):
    model = models.LicensedOperator
    form_class = forms.LicensedOperatorForm


class LicensedOperatorDetailView(generic.DetailView):
    model = models.LicensedOperator
    form_class = forms.LicensedOperatorForm


class LicensedOperatorUpdateView(generic.UpdateView):
    model = models.LicensedOperator
    form_class = forms.LicensedOperatorForm
    pk_url_kwarg = "pk"


class LicensedOperatorDeleteView(generic.DeleteView):
    model = models.LicensedOperator
    success_url = reverse_lazy("operator_LicensedOperator_list")



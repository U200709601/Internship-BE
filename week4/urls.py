from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("GlobalOperator", api.GlobalOperatorViewSet)
router.register("PortabilityDatabase", api.PortabilityDatabaseViewSet)

urlpatterns = (
    path("api/v1/", include(router.urls)),
    
    path("globaloperator/", views.GlobalOperatorListView.as_view({'get': 'list', 'post': 'create', 'put':'update', 'patch':'partial_update', 'delete':'destroy'}), name="operator_GlobalOperator_list"),
    path("globaloperator/create/", views.GlobalOperatorCreateView.as_view(), name="operator_GlobalOperator_create"),
    path("globaloperator/detail/<int:pk>/", views.GlobalOperatorDetailView.as_view(), name="operator_GlobalOperator_detail"),
    path("globaloperator/update/<int:pk>/", views.GlobalOperatorUpdateView.as_view(), name="operator_GlobalOperator_update"),
    path("globaloperator/delete/<int:pk>/", views.GlobalOperatorDeleteView.as_view(), name="operator_GlobalOperator_delete"),
    path("portabilitydatabase/", views.PortabilityDatabaseListView.as_view({'get': 'list', 'post': 'create', 'put':'update', 'patch':'partial_update', 'delete':'destroy'}), 
    
    
    path("portabilitydatabase/", views.PortabilityDatabaseListView.as_view({'get': 'list', 'post': 'create', 'put':'update', 'patch':'partial_update', 'delete':'destroy'}), name="operator_PortabilityDatabase_list"),
    path("portabilitydatabase/create/", views.PortabilityDatabaseCreateView.as_view(), name="operator_PortabilityDatabase_create"),
    path("portabilitydatabase/detail/<int:pk>/", views.PortabilityDatabaseDetailView.as_view(), name="operator_PortabilityDatabase_detail"),
    path("portabilitydatabase/update/<int:pk>/", views.PortabilityDatabaseUpdateView.as_view(), name="operator_PortabilityDatabase_update"),
    path("portabilitydatabase/delete/<int:pk>/", views.PortabilityDatabaseDeleteView.as_view(), name="operator_PortabilityDatabase_delete"),
)


 path("networkoperator/", views.NetworkOperatorListView.as_view({'get': 'list', 'post': 'create', 'put':'update', 'patch':'partial_update', 'delete':'destroy'}), name="operator_NetworkOperator_list"),
    path("networkoperator/create/", views.NetworkOperatorCreateView.as_view(), name="operator_NetworkOperator_create"),
    path("networkoperator/detail/<int:pk>/", views.NetworkOperatorDetailView.as_view(), name="operator_NetworkOperator_detail"),
    path("networkoperator/update/<int:pk>/", views.NetworkOperatorUpdateView.as_view(), name="operator_NetworkOperator_update"),
    path("networkoperator/delete/<int:pk>/", views.NetworkOperatorDeleteView.as_view(), name="operator_NetworkOperator_delete"),
    
     path("licensedoperator/", views.LicensedOperatorListView.as_view({'get': 'list', 'post': 'create', 'put':'update', 'patch':'partial_update', 'delete':'destroy'}), name="operator_LicensedOperator_list"),
    path("licensedoperator/create/", views.LicensedOperatorCreateView.as_view(), name="operator_LicensedOperator_create"),
    path("licensedoperator/detail/<int:pk>/", views.LicensedOperatorDetailView.as_view(), name="operator_LicensedOperator_detail"),
    path("licensedoperator/update/<int:pk>/", views.LicensedOperatorUpdateView.as_view(), name="operator_LicensedOperator_update"),
    path("licensedoperator/delete/<int:pk>/", views.LicensedOperatorDeleteView.as_view(), name="operator_LicensedOperator_delete"),
    
    

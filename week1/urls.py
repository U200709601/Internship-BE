from django.urls import path, include
from rest_framework import routers

from . import api
from . import views


router = routers.DefaultRouter()
router.register("GlobalOperator", api.GlobalOperatorViewSet)


urlpatterns = (
    path("api/v1/", include(router.urls)),
    path("globaloperator/", views.GlobalOperatorListView.as_view({'get': 'list', 'post': 'create', 'put':'update', 'patch':'partial_update', 'delete':'destroy'}), name="operator_GlobalOperator_list"),
    path("globaloperator/create/", views.GlobalOperatorCreateView.as_view(), name="operator_GlobalOperator_create"),
    path("globaloperator/detail/<int:pk>/", views.GlobalOperatorDetailView.as_view(), name="operator_GlobalOperator_detail"),
    path("globaloperator/update/<int:pk>/", views.GlobalOperatorUpdateView.as_view(), name="operator_GlobalOperator_update"),
    path("globaloperator/delete/<int:pk>/", views.GlobalOperatorDeleteView.as_view(), name="operator_GlobalOperator_delete"),
    path("portabilitydatabase/", views.PortabilityDatabaseListView.as_view({'get': 'list', 'post': 'create', 'put':'update', 'patch':'partial_update', 'delete':'destroy'}), 
)

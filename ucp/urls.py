from django.urls import path

from .views import ucp_index, ucp_worker_register, ucp_worker_view

urlpatterns = [
    path('', ucp_index),
    path('register/', ucp_worker_register),
    path('worker/<uuid:id>', ucp_worker_view),
]

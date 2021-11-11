from django.urls import path

from .views import ClientListView


urlpatterns = [
    path('list-clients', ClientListView.as_view(), name='clientList'),
    
]
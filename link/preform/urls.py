from django.urls import path
from preform.views import PreformCreateView, PreformListView


urlpatterns = [
    path('preform', PreformCreateView.as_view(), name='preformCreate'),
    path('list-preforms', PreformListView.as_view(), name='preformList'),
]
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse
from django.utils import timezone
# Importamos las platillas a utilizar 
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic import TemplateView 
# Importamos los decoradores
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
# Importamos los modelos
from preform.models import Branch, Preform

# Create your views here.

class PreformCreateView(CreateView):
    model = Preform
    fields = '__all__'
    success_url = reverse_lazy('customersList')

    @method_decorator(csrf_exempt)
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    # Sobreescribimos el metodo POST
    def post(self, request, *args, **kwargs):
        # Se crea un diccionario donde se enviara la data
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for c in Branch.objects.filter(name__icontains=request.POST['term'])[0:10]:
                    item = c.toJSON()
                    item['text'] = (c.name + ' - ' + c.company.name)
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['action'] = 'add'
        context["titulo"] = 'Preformas' 
        return context

class PreformListView(ListView):
    model = Preform
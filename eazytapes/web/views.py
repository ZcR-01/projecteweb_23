from django.shortcuts import render
from django.http import HttpResponse
from web.models import Bar, Tapa
from django.views import generic

# Create your views here. Html de la aplicació

#def principal(request):
#    bars = Bar.objects.all()
#    resposta = [bar.name for bar in bars]
#    html = "<br />".join(resposta)
#    return HttpResponse(html)

def principal(request):
    bars = Bar.objects.all()
    return render(request, 'web/index.html', {"bars": bars})

def bar(request, bar_id):
    bar = Bar.objects.get(pk=bar_id) #primary key
    return render(request, 'web/bar.html', {"bar": bar})



class TapaView(generic.DetailView):
    model = Tapa
    template_name = 'web/tapa.html'
from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from .models import Produto
from .forms import ProdutoForm



def produto_list(request):
    objects = Produto.objects.all()
    context = {'object_list': objects}
    return render(request, 'produto_list.html', context)


def produto_detail(request, pk):
    object = Produto.objects.get(pk=pk)
    context = {'object': object}
    return render(request, 'produto_detail.html', context)


'''def produto_add(request):
    template_name = 'produto_form.html'
    return render(request, template_name)
'''


class ProdutoCreate(CreateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm

class ProdutoUpdate(UpdateView):
    model = Produto
    template_name = 'produto_form.html'
    form_class = ProdutoForm

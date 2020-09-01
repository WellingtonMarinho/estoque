from django.shortcuts import render
from .models import Produto


def produto_list(request):
    objects = Produto.objects.all()
    context = {'object_list': objects}
    return render(request, 'produto_list.html', context)


def produto_detail(request, pk):
    object = Produto.objects.get(pk=pk)
    context = {'object': object}
    return render(request, 'produto_detail.html', context)


def produto_add(request):
    template_name = 'produto_form.html'
    return render(request, template_name)


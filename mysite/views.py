from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse_lazy
from board.models import Product, Category
from django.shortcuts import render

# class HomeView(TemplateView):
#     template_name = 'home.html'

def HomeView(request):
    category = request.GET.get("category")
    if category != None:
        products = Product.objects.filter(category__title = category)
    else:
        products = Product.objects.all()
    category = Category.objects.all()
    return render(request, 'board/product_list.html', {'products': products, 'category': category})


class UserRegisterView(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    # 타이밍 로딩 문제로 reverse를 사용시 에러가 발생
    success_url = reverse_lazy('register_done')


class UserRegisterDoneView(TemplateView):
    template_name = 'registration/register_done.html'

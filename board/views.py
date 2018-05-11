from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from board.models import Product, Category, Comment
from board.forms import CommentForm, ImgForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
import json
from django.http import HttpResponse
# Create your views here.







def product_list(request):
    category = request.GET.get("category")
    if category != None:
        products = Product.objects.filter(category__title = category)
    else:
        products = Product.objects.all()
    category = Category.objects.all()

    return render(request, 'board/product_list.html', {'products': products, 'category': category})

# def product_list(request):
#     if request.user.is_authenticated:
#         if request.user.is_vip:
#             return redirect('product:product_detail')
#         elif request.user.is_member:
#             return redirect('product:product_detail')
#         elif request.user.is_member:
#             return redirect('home')
#         else:
#             return render(request, 'about.html')
#     return render(request, 'home.html',{'cates':cate})



# class ProductListView(ListView):
#     model = Product


class ProductDetailView(DetailView):
    model = Product

class ProductCreateView(CreateView):
    form_class = ImgForm
    template_name = 'board/product_form.html'
    # model = Product
    # fields = ['writer', 'title','content','img']

class ProductUpdateView(UpdateView):
    model = Product
    fields = ['title', 'content', 'category', 'food','writer', 'img']
    template_name_suffix = '_update_form'
class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('product:product_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('product:product_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request,'board/add_comment_to_post.html',{'form': form})


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('product:product_detail', pk=comment.post.pk)
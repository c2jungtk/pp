from django import forms
from board.models import Product, Comment

# class Postform(forms.Form):
#     title = forms.CharField(max_length=200)
#     text = forms.Textarea()

# class PostForm(forms.ModelForm):
#
#     class Meta:
#         model =
#         fields = ('title', 'text',)

# class ProductForm(forms.ModelForm):
#     class Meta:
#         model = Product
#         fields = ('title','content')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text','author')

class ImgForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['writer', 'title','content', 'category', 'food','img']

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['writer', 'title','content', 'category', 'food','img']


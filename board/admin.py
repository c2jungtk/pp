from django.contrib import admin
from board.models import Product, Category, Food, Comment
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Food)
admin.site.register(Comment)
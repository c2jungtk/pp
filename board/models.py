from django.db import models
from account.models import Member
from django.urls import reverse
from django.utils import timezone
import os
# Create your models here.

class Food(models.Model):
    JAPANESE = 'J'
    CHINESE = 'C'
    KOREAN = 'K'
    EUROPEAN = 'E'
    FOOD_CHOICES = {
        (JAPANESE, '일식'),
        (CHINESE, '중식'),
        (KOREAN, '한식'),
        (EUROPEAN, '유럽식'),
    }
    title = models.CharField('음식',max_length=1, choices=FOOD_CHOICES)


    def __str__(self):
        return self.title

class Category(models.Model):
    COOK = 'CO'
    RECIPE = 'RE'
    DIET = 'DI'
    ACADEMY = 'AC'
    QUESTION = 'QU'
    CATEGORY_CHOICES = (
        (COOK, '요리자랑'),
        (RECIPE, '레시피'),
        (DIET, '오늘의식단'),
        (ACADEMY, '요리아카데미'),
        (QUESTION, '문의하기'),
    )
    title = models.CharField('카테고리', max_length=2, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title

# class Img(models.Model):
#     img = models.FileField(upload_to='images/%Y/%m/%d/', null=True)
#     created_date = models.DateTimeField(auto_now_add=True)
#
#     def filename(self):
#         return os.path.basename(self.img.name)


class Product(models.Model):
    writer = models.ForeignKey(Member, verbose_name='작성자')
    title = models.CharField('제목', max_length=30)
    content = models.TextField('내용')
    create_date = models.DateTimeField('작성일', auto_now_add=True)
    category = models.ForeignKey(Category)
    food = models.ForeignKey(Food)
    img = models.FileField(upload_to='images/%Y/%m/%d/', null=True,)


    def filename(self):
        return os.path.basename(self.img.name)

    def get_absolute_url(self):
        return reverse('product:product_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey('board.Product', related_name='comments')
    author = models.ForeignKey(Member)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True

        self.save()

    def __str__(self):
        return self.text



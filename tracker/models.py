from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from datetime import timedelta


# For newly created users
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# Create your models here.
class Category(models.Model):
    name  = models.CharField(max_length = 50 ,verbose_name = 'category name')

    def __str__(self):
        return f"{self.name}"

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', help_text='Choose the User to whom this budget belongs to', related_name='budgets')
    start_date = models.DateTimeField(blank=True, verbose_name='Start Date', default=now)
    end_date = models.DateTimeField(blank=True, verbose_name='End Date', default=now() + timedelta(days= 30))
    title = models.CharField(verbose_name='Title', max_length=100, help_text=' title of the Budget')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING) 
    cost = models.PositiveSmallIntegerField(verbose_name='Budget Cost', help_text='Enter the Budget amount:')
    
    def __str__(self):
        return f"{self.user} - {self.cost}"



class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='User', help_text='Choose the User to whom this expense belongs to', related_name='expenses')
    title = models.CharField(verbose_name='Title', max_length=100, help_text='A brief title of the expense')
    bill_date = models.DateField(blank=True, default=now, verbose_name='Bill Date')
    image = models.ImageField(blank=True, null=True, verbose_name='Image', upload_to='expense_image/', max_length=16384, help_text='Upload an Image')
    description = models.TextField(blank=True,verbose_name='Description', help_text='Enter the Description for the type of expense')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING,verbose_name = "Category")
    cost = models.PositiveSmallIntegerField(verbose_name='Expenditure Cost', help_text='Enter the Amount Expended')
    
    created = models.DateTimeField(blank=True,verbose_name='Created Date', auto_now=False, auto_now_add=True)
    modified = models.DateTimeField(blank=True,verbose_name='Modified Date', auto_now=True, auto_now_add=False)
    
    def __str__(self):
        return f"{self.user} - {self.title} - {self.category} - {self.cost} "
    
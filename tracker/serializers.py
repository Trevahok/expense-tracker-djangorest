from rest_framework import serializers
from django.contrib.auth.models import User
from . import models


class ExpenseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Expense
        fields = '__all__'

class BudgetSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Budget
        fields = '__all__'
    
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    budgets = BudgetSerializer(many=True)
    expenses = ExpenseSerializer(many=True)
    
    class Meta:
        depth = 1
        model = User
        fields = ('pk', 'username', 'email', 'budgets', 'expenses',)
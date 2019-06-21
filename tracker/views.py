from django.shortcuts import render
from rest_framework import viewsets, generics
from django.contrib.auth.models import User
from . import models
from . import serializers


class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing post instances.
    """
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class ExpenseViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing post instances.
    """
    serializer_class = serializers.ExpenseSerializer

    def get_queryset(self):
        return models.Expense.objects.filter(user = self.request.user)

class BudgetViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing post instances.
    """
    serializer_class = serializers.BudgetSerializer

    def get_queryset(self):
        return models.Budget.objects.filter(user = self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    serializer_class = serializers.UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        return User.objects.filter(username = self.request.user)
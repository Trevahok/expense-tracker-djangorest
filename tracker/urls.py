from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'category', views.CategoryViewSet)
router.register(r'budget', views.BudgetViewSet, basename='budget')
router.register(r'expense', views.ExpenseViewSet, basename= 'expense')
router.register(r'user', views.UserViewSet, basename='user')
urlpatterns = router.urls

# from django.urls import path

# urlpatterns += [
#     path('user')
# ]
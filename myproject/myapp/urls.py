from django.urls import path
from .views import index, register, iha_list, iha_add, iha_edit, iha_delete, rental_create, iha_list_search,customer_add,customers,customer_edit,customer_delete
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index', index, name='index'),
    path('', index, name='index'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', register, name='register'),
    path('ihalar/', iha_list, name='iha_list'),
    path('ihalar/add/', iha_add, name='iha_add'),
    path('ihalar/edit/<int:pk>/', iha_edit, name='iha_edit'),
    path('iha/<int:pk>/delete/', iha_delete, name='iha_delete'),
    path('ihalar/rent/<int:iha_id>/', rental_create, name='rental_create'),
    path('iha-list-search/', iha_list_search, name="ihalist_datatable"),
    path('customer/add/',customer_add, name='customer_add'),
    path('customers/',customers, name='customers'),
    path('customer/edit/<int:pk>/',customer_edit, name='customer_edit'),
    path('customer/delete/<int:pk>/',customer_delete, name='customer_delete'),
    
]
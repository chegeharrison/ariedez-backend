from django.urls import path
from . import views
from .views import ContactCreateView, ServiceListView, ServiceDetailView

urlpatterns = [
    path('services/', views.ServiceListView.as_view(), name='service-list'),
    path('<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('contact/', ContactCreateView.as_view(), name='contact-create'),
    path('contact/', views.contact_form, name='contact_form'),
]

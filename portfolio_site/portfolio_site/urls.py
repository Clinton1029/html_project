from django.contrib import admin
from django.urls import path, include
from .views import home_view, contact_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', contact_view, name='contact'),
    path('', home_view, name='home'),  # Home page
]
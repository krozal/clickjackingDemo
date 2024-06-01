from .views import clickjacking_demo
from django.contrib import admin
from django.urls import path
from .views import clickjacking_demo, target_page

urlpatterns = [
    path("admin/", admin.site.urls),
    path('clickjacking-demo/', clickjacking_demo, name='clickjacking_demo'),
    path('target-page/', target_page, name='target_page'),
]

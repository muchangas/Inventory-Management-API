from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # This line is the "bridge" to your inventory app
    path('api/v1/inventory/', include('inventory.urls')), 
    path('api-token-auth/', views.obtain_auth_token),
]
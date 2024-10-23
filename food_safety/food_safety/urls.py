from django.contrib import admin
from django.urls import path, include

app_name = 'food_analyser'

urlpatterns = [
    path('food_safety/', include('food_analyser.urls')),
    path('admin/', admin.site.urls),
]
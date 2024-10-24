from django.urls import path
from .views import IndexView, AnalysisView

app_name = 'food_analyser'

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('analysis/<int:food_id>', AnalysisView.as_view(), name='analysis'),
]
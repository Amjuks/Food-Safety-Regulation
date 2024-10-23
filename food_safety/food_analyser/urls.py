from django.urls import path
from .views import IndexView, AnalysisView

app_name = 'food_analyser'

urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('analysis/', AnalysisView.as_view(), name='analysis'),
]
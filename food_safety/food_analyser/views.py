import json

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

# Create your views here.
class IndexView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "food_analyser/index.html")

class AnalysisView(View):
    
    def post(self, request: HttpRequest) -> JsonResponse:

        content = {'success': False}

        try:
            image = None
            content['success'] = True

        except Exception as e:
            print(f"{type(e).__name__}: {e}")
            content['error_msg'] = f"{e}"

        return JsonResponse(content)
import os
import traceback

from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse

from pprint import pformat, pprint

from .models import AnalysedFood
from utils.analyse_food import encode_image, encode_memory_image, analyse_food

class IndexView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "food_analyser/index.html")

    def post(self, request: HttpRequest) -> JsonResponse:

        content = {'success': False}

        try:

            food_image = request.FILES['imageInput']
            
            food = AnalysedFood(image=food_image, report={})
            food.save()
            
            base64_image = encode_image(food.image.url[1:])
            report = analyse_food(f"data:{food_image.content_type};base64,{base64_image}")
            food.report = report
            food.save()

            content['success'] = True

        except Exception as e:
            print(f"{type(e).__name__}: {e}")
            content['error_msg'] = f"{e}"
            traceback.print_exc()

        return JsonResponse(content)
    
class AnalysisView(View):

    def get(self, request: HttpRequest, food_id: int) -> HttpResponse:
        context = {}
        try:
            context['food'] = AnalysedFood.objects.get(id=food_id)

        except AnalysedFood.DoesNotExist:
            return redirect(reverse('food_analyser:index'))
        
        return render(request, 'food_analyser/report.html', context=context)
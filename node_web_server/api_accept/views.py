from django.contrib.sites import requests
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response
import logging


# logger = logging.getLogger(__name__)
template_name = None
logger = logging.getLogger('data_logger')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('data.log')
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)


def log_api(request):
    if request.method == 'POST' and request.path == '/api/log':
        data = request.POST.get('data')

        if data:
            # Публикация данных в топике "recieved_data"
            publish_to_topic(data)


            if 'error' in data:
                logger.error(data)
            else:
                logger.info(data)

            return JsonResponse({'message': 'Data logged and published successfully'})
        else:
            return JsonResponse({'message': 'Invalid data'}, status=400)

    return render(request, 'log_form.html')


def publish_to_topic(data):
    # Имитация публикации данных в топике "recieved_data"
    print(f'Publishing data to topic /recieved_data: {data}')
    # Тут может быть код для ROS


class HomeView(View):
    def get(self, request):
        return HttpResponse("Welcome to the Home Page!")


# class LogAPIView(APIView):
#     def post(self, request):
#         data = request.data
#         if 'data' in data:
#             log_data = data['data']
#             if 'error' in log_data:
#                 logger.error(log_data)
#             else:
#                 logger.info(log_data)
#             return Response({'status': 'success'})
#         else:
#             return Response({'status': 'error', 'message': 'Invalid data format'})

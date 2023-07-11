from django.urls import include, path
from api_accept.views import  HomeView, log_api #LogAPIView,



# from django.contrib import admin
# from django.urls import path, include
# 
# urlpatterns = [
#       path('api/log', include('api_accept.urls')),
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('api/log', log_api, name='log_api'),
]

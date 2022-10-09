from rest_framework import routers
from django.urls import path, include
from ai.views import *


urls = [
      path('health/', getHealth),
      path('submitrequest/', submitRequest),
]
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, request
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.utils import json
import os
import openai

# Create your views here.
@api_view(['GET'])
def getHealth(request):
    return Response("ok")

@api_view(['POST'])
def submitRequest(request):
    data = request.data
    query = data['query']
    model= data['model']
    openai.api_key = "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"
    response = openai.Completion.create(
      model=model,
      prompt=query,
      temperature=0.7,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    return Response(response)
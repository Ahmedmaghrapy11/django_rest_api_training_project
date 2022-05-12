from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(["GET", "POST"])
def drinks_list(request, format = None):
    # check if it's a get method
    if request.method == "GET":
        # get all the drinks
        drinks = Drink.objects.all()
        # serialize all the drinks
        serializer = DrinkSerializer(drinks, many=True)
        # return json data
        return Response(serializer.data)
    # check if it's a post method
    if request.method == "POST":
        serilaizer = DrinkSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serilaizer.data, status = status.HTTP_201_CREATED)

@api_view(["GET", "PUT", "DELETE"])
def drink_detail(request, id, format=None):
    
    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Response(status= status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = DrinkSerializer(drink)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = DrinkSerializer(drink, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        drink.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
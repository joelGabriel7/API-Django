from django.http.response import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from countries.models import Countrie
from countries.serializer import CountriesSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def countries_list(request):
    if request.method == 'GET':
        countries = Countrie.objects.all()

        nombre = request.GET.get('nombre', None)
        if nombre is not None:
            countries = countries.filter(nombre__contains=nombre)

        countries_serializer = CountriesSerializer(countries, many=True)
        return JsonResponse(countries_serializer.data, safe=False)
        # Safe=False for objects serialzation


    elif request.method == 'POST':
        countries_data = JSONParser().parse(request)
        countries_serializer = CountriesSerializer(data=countries_data)
        if countries_serializer.is_valid():
            countries_serializer.save()
            return JsonResponse(countries_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(countries_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def countries_detail(request, pk):
    try:
        countries = Countrie.objects.get(pk=pk)
    except Countrie.DoesNotExist:
        return JsonResponse({'message': 'The country does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method =='GET':
        countries_serializer = CountriesSerializer(countries)
        return JsonResponse(countries_serializer.data)

    elif request.method == 'PUT':
        countries_data = JSONParser().parse(request)
        countries_serializer = CountriesSerializer(countries, data=countries_data)
        if countries_serializer.is_valid():
            countries_serializer.save()
            return JsonResponse(countries_serializer.data)
        return JsonResponse(countries_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        countries.delete()
        return JsonResponse({'message': 'Country was delete successfully!'}, status=status.HTTP_204_NO_CONTENT)



from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status

class FoodView(APIView):

    def get(self, request):

        food_type = request.query_params.get('food_type')


        if food_type and food_type.lower() in ['veg', 'non veg']:
            queryset = Items.objects.filter(food_type__iexact=food_type.lower())
        else:
            queryset = Items.objects.all()

        serializer = Items_Serializers(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request):

        serializer = Items_Serializers(data=request.data)

        if serializer.is_valid():

            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FoodViewById(APIView):


    def patch(self, request, id):

        try:
            item = Items.objects.get(id=id)

        except Items.DoesNotExist:
            return Response({"error": "Item not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = Items_Serializers(item, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

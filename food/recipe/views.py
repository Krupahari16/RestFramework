from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status

class FoodView(APIView):

    def get(self,request):

        all_items=Items.objects.all()

        serialized_food=Items_Serializers(all_items,many=True).data

        return Response(serialized_food)


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

from django.shortcuts import render
from .models import Syrius
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from django.http.response import JsonResponse
from rest_framework import status
import requests
from .models import Victorina
#----------------api-----------------------------      
#POST       
@api_view(["POST"])
def base64_image_upload_api_view(request):
    if request.method == "POST":
        data = request.data
        serializer = ImageBase64Serilizer(data=data)
        if serializer.is_valid():
            image = serializer.save()
            data = serializer.data
            return Response(data=data)
        return Response(serializer.errors, status=400)
     
#GET
@api_view(["GET"])
def syrius_list_published(request):
    images = Syrius.objects.all()
    
    if request.method == 'GET':
        images_serializer = ImageBase64Serilizer(images, many=True) 
        return JsonResponse(images_serializer.data, safe=False)


#DELETE
@api_view(["DELETE"])
def syrius_list_delete(request, pk):
    try:
        images = Syrius.objects.get(pk=pk)
    except Syrius.DoesNotExist:
        return JsonResponse({'message': 'The image does not found'}, status=status.HTTP_404_NOT_FOUND)
    

    if request.method == 'DELETE':
        images.delete()
        return JsonResponse({'message': 'Images was deleted successfully!'}, status = status.HTTP_204_NO_CONTENT)


#---------------Task 3----------------------------------------------------

class Test(APIView):
    # Task 3.1
    def __init__(self, x, y): 
        try:
            self.x = int(x)
            self.y = int(y)  
            
        except ValueError:
             ValueError(f'Arguments x = {x} or y = {y} is not a number')

    
    # Task 3.2
    def post(self, request):
        count = request.data.get('count')
        if request.method == "POST":
            victorins = requests.get('http://jservice.io/api/random', params={'count':count})                 
            data = victorins.json()
            for v in data:
                serializer = VictorinSerializator(data=v)
                cat_serializer = CategorySerializator(data=v.get('category'))
                if serializer.is_valid() and cat_serializer.is_valid():
                    
                    ids = serializer.validated_data['id']   #Проверка на уникальность в БД
                    if Victorina.objects.filter(id=ids).count()==1:  # Проверка на уникальность в БД
                        continue

                    serializer.save()
                    cat_serializer.save()
                    

            return Response({'post': f"{count} victorins added successfully!"})
    
    # Task 3.4
    def get(self, request):
        name = request.data.get('name')

        if type(name) == str:
            try:
                count = Category.objects.filter(title=name).count()
                
            except ValueError:
                ValueError('Argument is not correct')
            
            return Response({'message': f"There are {count} entries in the category"})
        else:
            return Response({'message': 'The category does not found'}, status=status.HTTP_404_NOT_FOUND)
        
    
    
            
            



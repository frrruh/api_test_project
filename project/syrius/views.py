from django.shortcuts import render
from .models import Syrius
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ImageBase64Serilizer
from django.http.response import JsonResponse
from rest_framework import status




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








# class SyriusAPIView(APIView):
#     def get(self, request): # получение ресура (чтение)
#         #получаем набор всех записей 
#         s = Syrius.objects.all()
#         return Response({'cars': SyriusSerialiazer(instance= s, many=True).data})
    
#     def post(self, request): #добавление новой записи 
#         serializer = SyriusSerialiazer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
        
#         return Response({'post': serializer.data})
    
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
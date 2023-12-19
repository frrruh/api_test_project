from .models import Syrius
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status, generics
import requests
from .models import Victorina
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from .permissions import IsAdminReadOnly, IsOwnerOrReadOnly
from rest_framework.pagination import PageNumberPagination
#----------------api-----------------------------      
# class SyriusViewSet(viewsets.ModelViewSet):
#     queryset = Syrius.objects.all()  
#     serializer_class = ImageBase64Serilizer

#     # def get_queryset(self): #Чтобы вывести определенное кол-во записей
#     #     return Syrius.objects.all()[:5]



class SyriusAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10000
    
class SyriusAPIList(generics.ListCreateAPIView):
    queryset = Syrius.objects.all()
    serializer_class = ImageBase64Serilizer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = SyriusAPIListPagination


class SyriusAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Syrius.objects.all()
    serializer_class = ImageBase64Serilizer
    permission_classes = (IsAuthenticated, )


class SyriusAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Syrius.objects.all()
    serializer_class = ImageBase64Serilizer
    permission_classes = (IsAdminReadOnly, )










#---------------API for external resource----------------------------------------------------

class Test(APIView):
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
        
    
    

class ImageAPIList(generics.ListCreateAPIView):
    queryset = Syrius.objects.all()
    serializer_class = ImageBase64Serilizer
            



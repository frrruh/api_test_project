from django.contrib import admin
from django.urls import path, include, re_path
from syrius.views import *
from rest_framework import routers



urlpatterns = [
    #  path("api/victorins/upload", Test.as_view()),
    # path("api/victorins/gets", Test.as_view()),
    # path('api/syriuslist/', SyriusViewSet.as_view({'get':'list'})),
    # path('api/syriusupdate/<int:pk>/', SyriusViewSet.as_view({'put':'update'})),
    # path('api/syriusdelete/<int:pk>/', SyriusViewSet.as_view({'delete':'destroy'})),
    # path('api/syriuscreate/', SyriusViewSet.as_view({'post':'create'})),
    path('api/drf-auth/', include('rest_framework.urls')),  # авторизация пользователей
    path('api/syrius/', SyriusAPIList.as_view()),
    path('api/syrius/<int:pk>/', SyriusAPIUpdate.as_view()),
    path('api/syriusdelete/<int:pk>/', SyriusAPIDestroy.as_view()),
    path('api/auth', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken'))
] 
from django.urls import path
from syrius.views import *



urlpatterns = [
    path("api/base64_image_upload/", base64_image_upload_api_view, name="base64_image_upload",),
    path("api/images/published/", syrius_list_published),
    path("api/images/<int:pk>", syrius_list_delete),
]
from django.contrib import admin
from django.urls import path,include
from .views import ExampleView,UserRegistrationView,FileDownloadView,FileUploadView


urlpatterns = [
    path('', ExampleView.as_view()),
    path('register/', UserRegistrationView.as_view(), name='user_registration'),
    path('upload/', FileUploadView.as_view(), name='file_upload'),
    path('download/<int:file_id>/', FileDownloadView.as_view(), name='file_download'),
]
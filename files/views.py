from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView,ListAPIView
from .serializers import UserRegistrationSerializer,FileUploadSerializer
from django.http import FileResponse
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status


from django.shortcuts import get_object_or_404
from .models import UploadedFile

class ExampleView(ListAPIView):
    

    # def get(self, request, format=None):
    #     content = {
    #         'user': str(request.user),  # `django.contrib.auth.User` instance.
    #         'auth': UploadedFile.objects.all(),  # None
    #     }
    #     return Response(content)
    queryset = UploadedFile.objects.all()
    serializer_class = FileUploadSerializer
    
class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

class FileUploadView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        serializer = FileUploadSerializer(data=request.data)

        if serializer.is_valid():
            # Set the user field to the logged-in user
            serializer.validated_data['user'] = self.request.user

            # Save the serializer to create the UploadedFile instance
            serializer.save()

            # You can save the file, process it, etc.
            # For example, saving the file to the media directory
            uploaded_file = serializer.validated_data['file']
            file_path = f'media/{uploaded_file.name}'
            with open(file_path, 'wb') as destination:
                for chunk in uploaded_file.chunks():
                    destination.write(chunk)

            return Response({'message': 'File uploaded successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FileDownloadView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, file_id):
        # Retrieve the uploaded file object from the database
        print("HEllo")
        uploaded_file = get_object_or_404(UploadedFile, id=file_id)

        # Open the file for download
        file_path = uploaded_file.file.path
        response = FileResponse(open(file_path, 'rb'))
        print(response)
        # Set the content type to the file's MIME type
        response['Content-Type'] = 'application/octet-stream'
        # Set the Content-Disposition header to force download
        response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
        print(response)

        return response
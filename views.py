# views.py

from rest_framework import generics, status
from rest_framework.response import Response
from .models import Conversation, UploadedFile
from .serializers import ConversationSerializer, UploadedFileSerializer

class ConversationSummaryAPIView(generics.ListAPIView):
    serializer_class = ConversationSerializer
    queryset = Conversation.objects.all()
    pagination_class = YourPaginationClass  # Use DRF pagination class

    def get_queryset(self):
        # Implement filtering logic if needed
        return super().get_queryset()

class FileUploadAPIView(generics.CreateAPIView):
    serializer_class = UploadedFileSerializer

    def perform_create(self, serializer):
        # Implement file duplication check logic
        instance = serializer.save()
        # Handle file storage and database entry

class UploadedFilesListAPIView(generics.ListAPIView):
    serializer_class = UploadedFileSerializer
    queryset = UploadedFile.objects.all()

class FileDeleteAPIView(generics.DestroyAPIView):
    queryset = UploadedFile.objects.all()

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # Delete file from storage
        instance.file.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

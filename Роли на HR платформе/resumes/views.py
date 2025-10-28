from rest_framework import viewsets
from .models import Resume
from .serializers import ResumeSerializer
from .permissions import ResumePermission

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [ResumePermission]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.role == user.CANDIDATE:
            return self.queryset.filter(user=user)
        elif user.role == user.HR_MANAGER:
            return self.queryset
        elif user.role == user.ADMIN:
            return self.queryset
        else:
            return self.queryset.none()
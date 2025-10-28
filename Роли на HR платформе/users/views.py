from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer
from .models import User

class UserRegistrationView(CreateAPIView):
    permission_classes = []
    queryset = User.objects.all()
    serializer_class = UserSerializer

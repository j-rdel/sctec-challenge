from rest_framework.viewsets import ModelViewSet
from .models import Enterprise
from .serializers import EnterpriseSerializer


class EnterpriseViewSet(ModelViewSet):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer

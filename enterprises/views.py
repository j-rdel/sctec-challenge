from rest_framework.viewsets import ModelViewSet

from core.pagination import DefaultPagination
from enterprises.filters import EnterpriseFilter
from enterprises.models import Enterprise
from enterprises.serializers import EnterpriseSerializer, EnterpriseListSerializer


class EnterpriseViewSet(ModelViewSet):
    queryset = Enterprise.objects.all()
    serializer_class = EnterpriseSerializer
    pagination_class = DefaultPagination
    filterset_class = EnterpriseFilter

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return EnterpriseListSerializer

        return EnterpriseSerializer

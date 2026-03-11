from rest_framework import serializers

from core.enums import STATUS_CHOICES
from core.serializers import ChoiceDisplayField
from .enums import BUSINESS_SEGMENT_CHOICES
from .models import Enterprise


class EnterpriseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enterprise
        fields = "__all__"


class EnterpriseListSerializer(EnterpriseSerializer):
    segment = ChoiceDisplayField(choices=BUSINESS_SEGMENT_CHOICES)
    status = ChoiceDisplayField(choices=STATUS_CHOICES)

    class Meta:
        model = Enterprise
        fields = "__all__"

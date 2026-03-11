from django_filters import CharFilter, ChoiceFilter

from core.filters import DateRangeFilter, StatusFilter
from enterprises.enums import BUSINESS_SEGMENT_CHOICES
from enterprises.models import Enterprise


class EnterpriseFilter(DateRangeFilter, StatusFilter):
    name = CharFilter(lookup_expr='icontains')
    entrepreneur_name = CharFilter(lookup_expr='icontains')
    municipality = CharFilter(lookup_expr='icontains')
    segment = ChoiceFilter(choices=BUSINESS_SEGMENT_CHOICES)
    contact_email = CharFilter(lookup_expr='icontains')

    class Meta:
        model = Enterprise
        fields = [
            "name", "entrepreneur_name", "municipality", "segment", "contact_email", "status", "created_after",
            "created_before", "updated_after", "updated_before"
        ]

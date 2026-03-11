from django_filters import ChoiceFilter, FilterSet, DateTimeFilter

from core.enums import STATUS_CHOICES


class DateRangeFilter(FilterSet):
    created_after = DateTimeFilter(field_name="created_at", lookup_expr="gte")
    created_before = DateTimeFilter(field_name="created_at", lookup_expr="lte")
    updated_after = DateTimeFilter(field_name="updated_at", lookup_expr="gte")
    updated_before = DateTimeFilter(field_name="updated_at", lookup_expr="lte")


class StatusFilter(FilterSet):
    status = ChoiceFilter(choices=STATUS_CHOICES)

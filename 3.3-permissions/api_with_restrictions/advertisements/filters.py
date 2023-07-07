from django_filters import rest_framework as filters

from advertisements.models import Advertisement


class AdvFilter(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['creator', 'status', 'created_at']
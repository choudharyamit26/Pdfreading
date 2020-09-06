import django_filters
from src.models import DailyRenewableGenerationReport, DailyRenewableGenerationReportISGS, StateControlArea
from django_filters import DateFilter


class DailyRenewableGenerationReportFilter(django_filters.FilterSet):
    from_date = DateFilter(field_name='date', lookup_expr='gte', label='From Date')
    to_date = DateFilter(field_name='date', lookup_expr='lte', label='To Date')

    class Meta:
        model = DailyRenewableGenerationReport
        fields = ('from_date', 'to_date')


class DailyRenewableGenerationReportISGSFilter(django_filters.FilterSet):
    from_date = DateFilter(field_name='date', lookup_expr='gte', label='From Date')
    to_date = DateFilter(field_name='date', lookup_expr='lte', label='To Date')

    class Meta:
        model = DailyRenewableGenerationReportISGS
        fields = ('from_date', 'to_date')


class StateControlAreaFilter(django_filters.FilterSet):
    from_date = DateFilter(field_name='date', lookup_expr='gte', label='From Date')
    to_date = DateFilter(field_name='date', lookup_expr='lte', label='To Date')

    class Meta:
        model = StateControlArea
        fields = ('from_date', 'to_date')

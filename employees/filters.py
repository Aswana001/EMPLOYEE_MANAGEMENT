import django_filters
from .models import Employee


class EmployeeFilter(django_filters.FilterSet):
    department = django_filters.NumberFilter(field_name='department_id')
    designation = django_filters.NumberFilter(field_name='designation_id')
    is_active = django_filters.BooleanFilter(field_name='is_active')

    class Meta:
        model = Employee
        fields = ['department', 'designation', 'is_active']
from django.urls import path
from .views import (
    DepartmentListCreateView,
    DepartmentRetrieveUpdateDestroyView,
    DesignationListCreateView,
    DesignationRetrieveUpdateDestroyView,
    EmployeeListCreateView,
    EmployeeRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('departments/', DepartmentListCreateView.as_view(), name='department-list-create'),
    path('departments/<int:pk>/', DepartmentRetrieveUpdateDestroyView.as_view(), name='department-detail'),

    path('designations/', DesignationListCreateView.as_view(), name='designation-list-create'),
    path('designations/<int:pk>/', DesignationRetrieveUpdateDestroyView.as_view(), name='designation-detail'),

    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-detail'),
]
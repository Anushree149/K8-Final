import django_filters
from . models import Todo
from django import forms
from django_filters import DateFilter,CharFilter




class TodoFilter(django_filters.FilterSet):

    exact_date = DateFilter(field_name='deadline',lookup_expr='exact',label= "Enter Deadline",widget=forms.DateInput(attrs={'placeholder':"YYYY-MM-DD"}))
    assign_to = CharFilter(field_name='search',lookup_expr='icontains',label= "Employee Name")
    Search_employee = CharFilter(field_name='title', lookup_expr='icontains',label= "Enter Task Name")
    Task_priority = CharFilter(field_name='priority', lookup_expr='icontains',label= "Task Priority")
    class Meta:
        model = Todo
        fields = '__all__'
        exclude =['task','slug','deadline','title','search','status','company_name']    

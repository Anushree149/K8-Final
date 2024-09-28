import django_filters
from . models import Account
from django import forms
from django_filters import DateFilter,CharFilter

class NameFilter(django_filters.FilterSet):
    
    Search_Name = CharFilter(field_name='first_name',lookup_expr="icontains",widget=forms.TextInput(attrs={'style':'width:100%;','placeholder':"Enter name"}) ,label="Enter Name")
    class Meta:
        model = Account
        fields = "__all__"

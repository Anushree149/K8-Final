from django import forms
from accounts.models import *
from . models import Todo,Feedback

class DateInput(forms.DateInput):
    input_type = "date"


    
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        widgets = {'deadline':DateInput()}

        fields = ['assign_to','title','task','deadline','status','priority']
        
        labels = {'title':"Task" , 'task':'Task Details'}
        exclude = ('search','company_name')
    


    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Filter the authors based on the user.
        self.fields['assign_to'].queryset = Account.objects.filter(company_name=user.company_name,is_admin=False)
        

class SpecificFieldUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"
        exclude = ('assign_to','search','search','company_name')
        # fields = ['status','remark']
    # assign_to = forms.CharField(disabled=True)
    title = forms.CharField(disabled=True)
    task = forms.CharField(disabled=True)
    deadline = forms.CharField(disabled=True)
    priority = forms.CharField(disabled=True)
    # sta = forms.CharField(disabled=True)


class AllFieldUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['assign_to','title','task','deadline','status','priority']
    
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Filter the authors based on the user.
        self.fields['assign_to'].queryset = Account.objects.filter(company_name=user.company_name,is_admin=False)



class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['experience','type','feedback']
        labels = {'type':"Feedback Type"}
        exclude = ('user',)



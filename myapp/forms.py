from django import forms
from .models import Budget, company, employee_info, Hotel

class CompanyForm(forms.ModelForm):
    class Meta:
        model = company
        fields = ['com_id', 'cname']

class EmployeeInfoForm(forms.ModelForm):
    class Meta:
        model = employee_info
        fields = [
            'em_Id', 'em_Name', 'em_Mobile', 'em_Salary', 'em_Email',
            'em_Birth_Date', 'em_Join_Date', 'em_Desin', 'em_Dept', 'com_Id'
        ]
        widgets = {
            'em_Birth_Date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'em_Join_Date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ['name', 'hotel_Main_Img']
        
class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget    
        fields = '__all__'

        
                    
from django import forms
from .models import Programme, Department
from .models import Room

class ProgramForm(forms.ModelForm):
    # Choices for level field
    LEVEL_CHOICES =[
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
        ('FYUG','Four year UG'),
        ('IPG','Integrated PG'),
    ]
    
    # Dropdown for level field
    level = forms.ChoiceField(
        choices=LEVEL_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    # Dropdown for department field, linked to the Department table
    dept = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        empty_label="Select Department"
    )

    class Meta:
        model = Programme
        fields = ['programme_name', 'dept', 'level', 'duration']
        widgets = {
            'programme_name': forms.TextInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
        }

from .models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['room_no', 'no_of_rows', 'no_of_columns', 'block_no']
        widgets = {
            'room_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Room Number'}),
            'no_of_rows': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Rows'}),
            'no_of_columns': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Number of Columns'}),
            'block_no': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Block Number'}),
        }
        labels = {
            'room_no': 'Room Number',
            'no_of_rows': 'Number of Rows',
            'no_of_columns': 'Number of Columns',
            'block_no': 'Block Number',
        }

from django import forms
from .models import Programme, Department
from .models import Room,Course,Exam
from .models import Timetable
from .models import Teacher
from .models import DutyAllotment

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


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'course_code', 
            'course_title', 
            'pgm', 
            'exam_duration', 
            'sem', 
            'syllabus_year'
        ]
        widgets = {
            'course_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Course Code'}),
            'course_title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Course Title'}),
            'pgm': forms.Select(attrs={'class': 'form-control'}),
            'exam_duration': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Exam Duration'}),
            'sem': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Semester'}),
            'syllabus_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Syllabus Year'}),
        }
        labels = {
            'course_code': 'Course Code',
            'course_title': 'Course Title',
            'pgm': 'Programme',
            'exam_duration': 'Exam Duration',
            'sem':'Semester',
            'syllabus_year':'Syllabus Year',
        }


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['sem', 'year', 'level', 'active', 'month']
        widgets = {
            'sem': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Semester'}),
            'year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Year'}),
            'level': forms.Select(choices=[
            ('UG', 'Undergraduate'),
            ('PG', 'Postgraduate'),
            ('FYUG','Four year UG'),
            ('IPG','Integrated PG')
            ], attrs={'class': 'form-control'}),
            'active': forms.Select(choices=[
                (True, 'Yes'),
                (False, 'No')
            ], attrs={'class': 'form-control'}),
            'month': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Month'}),
        }
        labels = {
            'sem': 'Semester',
            'year': 'Year',
            'level': 'Level',
            'active': 'Active',
            'month': 'Month',
        }

class TimetableForm(forms.ModelForm):
    SESSION_CHOICES = [
        ('Forenoon', 'Forenoon'),
        ('Afternoon', 'Afternoon'),
    ]

    session = forms.ChoiceField(choices=SESSION_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))  # ✅ Use Select widget

    class Meta:
        model = Timetable
        fields = ['exam', 'course', 'date', 'session']
        widgets = {
            'exam': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import Teacher, Department  # Make sure you import your models

# You can validate phone number with regular expression (if needed)
import re
def validate_phone(value):
    if not re.match(r'^\d{10}$', value):
        raise forms.ValidationError('Invalid phone number. Please enter a 10-digit number.')

class TeacherForm(UserCreationForm):
    # Define form fields for the teacher's details
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(required=True)
    phone_num = forms.CharField(max_length=10, required=True, validators=[validate_phone])
    designation = forms.ChoiceField(choices=Teacher.DESIGNATION_CHOICES, required=True)
    gender = forms.ChoiceField(choices=Teacher.GENDER_CHOICES,required=True)
    dept = forms.ModelChoiceField(queryset=Department.objects.all(), required=True)
    role = forms.ChoiceField(choices=[('Teacher', 'Teacher'), ('Examination Chief', 'Examination Chief')], required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit=True):
        # Save the User model
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
            # Create the Teacher profile
            teacher = Teacher.objects.create(
                user=user,
                phone_num=self.cleaned_data['phone_num'],
                designation=self.cleaned_data['designation'],
                gender=self.cleaned_data['gender'],
                dept=self.cleaned_data['dept']
            )
            
            # Assign the user to a group based on the selected role
            role = self.cleaned_data['role']
            if role == 'Examination Chief':
                group = Group.objects.get(name='Examination Chief')
                user.is_staff = True  # Make the user a staff member (admin level)
            else:
                group = Group.objects.get(name='Teacher')
            
            user.groups.add(group)  # Add the user to the selected group
            user.save()  # Save the user after assigning group

        return user

class DutyAllotmentForm(forms.ModelForm):
    class Meta:
        model = DutyAllotment
        fields = ['teacher', 'date', 'room', 'hours']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Optional: custom widget for date input
        }

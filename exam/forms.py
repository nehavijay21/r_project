from django import forms
from .models import Programme, Department
from .models import Room,Course,Exam
from .models import Timetable
from .models import Teacher
from .models import Dutyallot

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

    session = forms.ChoiceField(choices=SESSION_CHOICES, widget=forms.Select())  # ✅ Use Select widget

    class Meta:
        model = Timetable
        fields = ['exam', 'course', 'date', 'session']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['teacher_name', 'dept']  # Exclude user_id if you want it auto-generated

    def __init__(self, *args, **kwargs):
        super(TeacherForm, self).__init__(*args, **kwargs)
        # You can add custom logic here if needed
# forms.py


class DutyallotForm(forms.ModelForm):
    class Meta:
        model = Dutyallot
        fields = ['teacher', 'date', 'room', 'hours']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),  # Optional: custom widget for date input
        }

from django.shortcuts import render, get_object_or_404, redirect
from .models import Programme
from .forms import ProgramForm
from .models import Room
from .forms import RoomForm
from .models import Course
from .forms import CourseForm
from .models import Exam
from .forms import ExamForm
from .models import Timetable
from .forms import TimetableForm
from .models import Teacher
from .forms import TeacherForm
from .models import DutyAllotment
from .forms import DutyAllotmentForm
from django.contrib.auth.decorators import login_required


@login_required()
def index(request):
    return render(request, 'index.html')

def manage_programs(request):
    return render(request, 'manage_programs.html')

def manage_rooms(request):
    return render(request, 'manage_rooms.html')

def manage_course(request):
    return render(request, 'manage_course.html')

def manage_exam(request):
    return render(request, 'manage_exam.html')

def manage_timetable(request):
    return render(request, 'manage_timetable.html')

def manage_teacher(request):
    return render(request, 'manage_teacher.html')
# Add more views as needed

def manage_dutyallot(request):
    return render(request, 'manage_dutyallot.html')

def program_list(request):
    programs = Programme.objects.all()
    return render(request, 'program_list.html', {'programs': programs})

def add_program(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('program_list')
    else:
        form = ProgramForm()
    return render(request, 'add_program.html', {'form': form})

def edit_program(request, pk):
    program = get_object_or_404(Programme, pk=pk)
    if request.method == 'POST':
        form = ProgramForm(request.POST, instance=program)
        if form.is_valid():
            form.save()
            return redirect('program_list')
    else:
        form = ProgramForm(instance=program)
    return render(request, 'add_program.html', {'form': form})

def delete_program(request, pk):
    program = get_object_or_404(Programme, pk=pk)
    if request.method == 'POST':
        program.delete()
        return redirect('program_list')
    return render(request, 'delete_program.html', {'program': program})

##########################

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})

def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm()
    return render(request, 'add_room.html', {'form': form})

def edit_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm(instance=room)
    return render(request, 'add_room.html', {'form': form})

def delete_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')
    return render(request, 'delete_room.html', {'room': room})

# from django.contrib.auth.decorators import login_required

 # @login_required
# def dashboard(request):
 #     return render(request, 'index.html')

def course_list(request):
    course = Course.objects.all()
    return render(request, 'course_list.html', {'course': course})

def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})

def edit_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'add_course.html', {'form': form})

def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'delete_course.html', {'course': course})

##################################

def exam_list(request):
    exam = Exam.objects.all()
    return render(request, 'exam_list.html', {'exam': exam})

def add_exam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exam_list')
    else:
        form = ExamForm()
    return render(request, 'add_exam.html', {'form': form})

def edit_exam(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    if request.method == 'POST':
        form = ExamForm(request.POST, instance=exam)
        if form.is_valid():
            form.save()
            return redirect('exam_list')
    else:
        form = ExamForm(instance=exam)
    return render(request, 'add_exam.html', {'form': form})

def delete_exam(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    if request.method == 'POST':
        exam.delete()
        return redirect('exam_list')
    return render(request, 'delete_exam.html', {'exam': exam})


def timetable_list(request):
    timetable= Timetable.objects.all()
    return render(request, 'timetable_list.html', {'timetable': timetable})

def add_timetable(request):
    if request.method == 'POST':
        form = TimetableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('timetable_list')
    else:
        form = TimetableForm()
    return render(request, 'add_timetable.html', {'form': form})

def edit_timetable(request, pk):
    timetable= get_object_or_404(Timetable, pk=pk)
    if request.method == 'POST':
        form = TimetableForm(request.POST, instance=timetable)
        if form.is_valid():
            form.save()
            return redirect('timetable_list')
    else:
        form = TimetableForm(instance=timetable)
    return render(request, 'add_timetable.html', {'form': form})

def delete_timetable(request, pk):
    timetable= get_object_or_404(Timetable, pk=pk)
    if request.method == 'POST':
        timetable.delete()
        return redirect('timetable_list')
    return render(request, 'delete_timetable.html', {'timetable': timetable})

#################################

def teacher_list(request):
    teacher= Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teacher': teacher})

def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            teacher = form.save(commit=False)
            teacher.user_id = request.user.id  # Assign user_id from logged-in user
            teacher.save()
            return redirect('teacher_list') 
    else:
        form = TeacherForm()
    return render(request, 'add_teacher.html', {'form': form})

def edit_teacher(request, pk):
    teacher= get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'add_teacher.html', {'form': form})

def delete_teacher(request, pk):
    teacher= get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'delete_teacher.html', {'teacher': teacher})

############################


def dutyallot_list(request):
    dutyallot= DutyAllotment.objects.all()
    return render(request, 'dutyallot_list.html', {'dutyallot': dutyallot})

def add_dutyallot(request):
    if request.method == 'POST':
        form = DutyAllotmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dutyallot_list')
    else:
        form = DutyAllotmentForm()
    return render(request, 'add_dutyallot.html', {'form': form})

def edit_dutyallot(request, pk):
    dutyallot= get_object_or_404(DutyAllotment, pk=pk)
    if request.method == 'POST':
        form = DutyAllotmentForm(request.POST, instance=dutyallot)
        if form.is_valid():
            form.save()
            return redirect('dutyallot_list')
    else:
        form = DutyAllotmentForm(instance=dutyallot)
    return render(request, 'add_dutyallot.html', {'form': form})

def delete_dutyallot(request, pk):
    dutyallot= get_object_or_404(DutyAllotment, pk=pk)
    if request.method == 'POST':
        dutyallot.delete()
        return redirect('dutyallot_list')
    return render(request, 'delete_dutyallot.html', {'dutyallot': dutyallot})


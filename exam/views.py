from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.utils.timezone import now
from .models import Programme, Room, Course, Exam, Timetable, Teacher, DutyAllotment, DutyPreference
from .forms import ProgramForm, RoomForm, CourseForm, ExamForm, TimetableForm, TeacherForm, DutyAllotmentForm, DutyPreferenceForm
from datetime import datetime



@login_required()
def index(request):
    return render(request, 'index.html')

@login_required()
def manage_programs(request):
    return render(request, 'manage_programs.html')

@login_required()
def manage_rooms(request):
    return render(request, 'manage_rooms.html')

@login_required()
def manage_course(request):
    return render(request, 'manage_course.html')

@login_required()
def manage_exam(request):
    return render(request, 'manage_exam.html')

@login_required()
def manage_timetable(request):
    return render(request, 'manage_timetable.html')

@login_required()
def manage_teacher(request):
    return render(request, 'manage_teacher.html')

@login_required()
def manage_duty(request):
    duties = DutyAllotment.objects.all()  # Fetch duty allotments from database
    return render(request, 'duty_allotment.html', {'duties': duties})

@login_required()
def manage_preference(request):
    return render(request, 'manage_preference.html')

def chief_group_required(user):
    return user.groups.filter(name='Chief').exists()

def teacher_group_required(user):
    return user.groups.filter(name='Teacher').exists()

@login_required
def dashboard_view(request):
    user = request.user
    is_teacher = user.groups.filter(name='teacher').exists()
    is_chief = user.groups.filter(name='chief').exists()

    # Fetch ongoing exams based on Timetable dates
    ongoing_exams = Exam.objects.filter(timetable__date__gte=now().date()).distinct()

    # Fetch duty allotments and preferences for teachers
    if is_teacher:
        duty_allotments = DutyAllotment.objects.filter(teacher=user.teacher)
        duty_preferences = DutyPreference.objects.filter(teacher=user.teacher)
    else:  # Chief sees everything
        duty_allotments = DutyAllotment.objects.all()
        duty_preferences = DutyPreference.objects.all()

    context = {
        'is_teacher': is_teacher,
        'is_chief': is_chief,
        'ongoing_exams': ongoing_exams,
        'duty_allotments': duty_allotments,
        'duty_preferences': duty_preferences
    }
    return render(request, 'index.html', context)
    
@login_required()
@user_passes_test(chief_group_required)
def program_list(request):
    programs = Programme.objects.all()
    return render(request, 'program_list.html', {'programs': programs})

@login_required()
@user_passes_test(chief_group_required)
def add_program(request):
    if request.method == 'POST':
        form = ProgramForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('program_list')
    else:
        form = ProgramForm()
    return render(request, 'add_program.html', {'form': form})

@login_required()
@user_passes_test(chief_group_required)
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

@login_required()
@user_passes_test(chief_group_required)
def delete_program(request, pk):
    program = get_object_or_404(Programme, pk=pk)
    if request.method == 'POST':
        program.delete()
        return redirect('program_list')
    return render(request, 'delete_program.html', {'program': program})

@login_required()
@user_passes_test(chief_group_required)
def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'room_list.html', {'rooms': rooms})

@login_required()
@user_passes_test(chief_group_required)
def add_room(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('room_list')
    else:
        form = RoomForm()
    return render(request, 'add_room.html', {'form': form})

@login_required()
@user_passes_test(chief_group_required)
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

@login_required()
@user_passes_test(chief_group_required)
def delete_room(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')
    return render(request, 'delete_room.html', {'room': room})

@login_required()
@user_passes_test(chief_group_required)
def course_list(request):
    course = Course.objects.all()
    return render(request, 'course_list.html', {'course': course})

@login_required()
@user_passes_test(chief_group_required)
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})

@login_required()
@user_passes_test(chief_group_required)
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

@login_required()
@user_passes_test(chief_group_required)
def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('course_list')
    return render(request, 'delete_course.html', {'course': course})


@login_required()
@user_passes_test(chief_group_required)
def exam_list(request):
    exam = Exam.objects.all()
    return render(request, 'exam_list.html', {'exam': exam})

@login_required()
@user_passes_test(chief_group_required)
def add_exam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exam_list')
    else:
        form = ExamForm()
    return render(request, 'add_exam.html', {'form': form})

@login_required()
@user_passes_test(chief_group_required)
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

@login_required()
@user_passes_test(chief_group_required)
def delete_exam(request, pk):
    exam = get_object_or_404(Exam, pk=pk)
    if request.method == 'POST':
        exam.delete()
        return redirect('exam_list')
    return render(request, 'delete_exam.html', {'exam': exam})

@login_required()
@user_passes_test(chief_group_required)
def timetable_list(request):
    timetable= Timetable.objects.all()
    return render(request, 'timetable_list.html', {'timetable': timetable})

@login_required()
@user_passes_test(chief_group_required)
def add_timetable(request):
    if request.method == 'POST':
        form = TimetableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('timetable_list')
    else:
        form = TimetableForm()
    return render(request, 'add_timetable.html', {'form': form})

@login_required()
@user_passes_test(chief_group_required)
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

@login_required()
@user_passes_test(chief_group_required)
def delete_timetable(request, pk):
    timetable= get_object_or_404(Timetable, pk=pk)
    if request.method == 'POST':
        timetable.delete()
        return redirect('timetable_list')
    return render(request, 'delete_timetable.html', {'timetable': timetable})

@login_required()
@user_passes_test(chief_group_required)
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teacher_list.html', {'teachers': teachers})

from django.contrib import messages

@login_required()
@user_passes_test(chief_group_required)
def add_teacher(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Teacher added successfully!")
                return redirect('teacher_list')  # Redirect to the teacher list page
            except Exception as e:
                messages.error(request, f"Error saving teacher: {e}")
                print(f"Error saving teacher: {e}")  # Print the error to console for debugging
        else:
            messages.error(request, "Form is invalid. Please check the entered data.")
            print("Form Errors: ", form.errors)  # Print errors to the console for debugging
    
    else:
        form = TeacherForm()
    
    return render(request, 'add_teacher.html', {'form': form})



@login_required()
@user_passes_test(chief_group_required)
def edit_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher.user)  # Access the User model
        if form.is_valid():
            form.save()
            return redirect('teacher_list')  # Redirect after successful edit
    else:
        form = TeacherForm(instance=teacher.user)  # Use the instance for the form
    return render(request, 'add_teacher.html', {'form': form})

@login_required()
@user_passes_test(chief_group_required)
def delete_teacher(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == 'POST':
        teacher.user.delete()  # Delete the related user as well
        return redirect('teacher_list')  # Redirect to teacher list after deletion
    return render(request, 'delete_teacher.html', {'teacher': teacher})

@login_required()
@user_passes_test(chief_group_required)
def duty_allotment(request):
    # Fetch all examination dates from the Timetable model
    exam_dates = Timetable.objects.all().order_by('date')

    # Count the number of duties assigned for each exam date
    duty_counts = {date.date: DutyAllotment.objects.filter(date=date.date).count() for date in exam_dates}

    return render(request, 'duty_allotment.html', {'exam_dates': exam_dates, 'duty_counts': duty_counts})

@login_required()
@user_passes_test(chief_group_required)
def manage_duty_allotments(request):
    selected_date = request.GET.get('date')  # Get date from the URL parameter
    if selected_date:
        duties = DutyAllotment.objects.filter(date=selected_date)  # Filter duties by selected date
    else:
        duties = DutyAllotment.objects.all()  # Show all duties if no date is selected

    return render(request, 'manage_duty_allotments.html', {'duties': duties, 'selected_date': selected_date})


@login_required()
@user_passes_test(chief_group_required)
def duty_list(request):
    date_str = request.GET.get('date')  # Get the date from URL parameters
    formatted_date = None  # Initialize formatted_date

    if date_str:
        try:
            # Convert 'Feb. 19, 2025' → 'YYYY-MM-DD'
            formatted_date = datetime.strptime(date_str, "%b. %d, %Y").date()
        except ValueError:
            formatted_date = None  # If conversion fails, return None

    # Query duties for the selected date, but only show duties where a teacher is assigned
    if formatted_date:
        duties = DutyAllotment.objects.filter(date=formatted_date, teacher__isnull=False)
    else:
        duties = []

    return render(request, 'duty_list.html', {'duties': duties, 'selected_date': date_str})

@login_required
@user_passes_test(chief_group_required)
def add_duty(request):
    selected_date = request.GET.get('date', datetime.today().strftime('%Y-%m-%d'))  # Get date from URL or use today

    if request.method == 'POST':
        print("✅ POST request received!")  # Debugging
        print("🔹 POST Data:", request.POST)  # Print form data

        form = DutyAllotmentForm(request.POST)
        if form.is_valid():
            try:
                duty = form.save(commit=False)  # Don't save yet
                duty.date = selected_date  # Assign the selected date manually
                duty.save()  # Save the duty
                messages.success(request, "Duty allotted successfully!")
                print("✅ Duty saved successfully!")
                return redirect('duty_list')  # Redirect after saving
            except Exception as e:
                messages.error(request, f"Error saving duty: {e}")
                print(f"❌ Error saving duty: {e}")  # Log error
        else:
            messages.error(request, "Form is invalid. Please check the entered data.")
            print("❌ Form Errors:", form.errors)  # Debugging form errors
    else:
        form = DutyAllotmentForm()
        print("🔹 GET request received")  # Debugging

    return render(request, 'add_duty.html', {'form': form, 'selected_date': selected_date})

@login_required()
@user_passes_test(chief_group_required)
def edit_duty(request, pk):
    duty = get_object_or_404(DutyAllotment, pk=pk)
    if request.method == 'POST':
        form = DutyAllotmentForm(request.POST, instance=duty)
        if form.is_valid():
            form.save()
            return redirect('duty_list')
    else:
        form = DutyAllotmentForm(instance=duty)
    return render(request, 'add_duty.html', {'form': form})

@login_required()
@user_passes_test(chief_group_required)
def delete_duty(request, pk):
    duty = get_object_or_404(DutyAllotment, pk=pk)
    if request.method == 'POST':
        duty.delete()
        return redirect('duty_list')
    return render(request, 'delete_duty.html', {'duty': duty})

@login_required()
def preference_list(request):
    preferences = DutyPreference.objects.all()
    return render(request, 'preference_list.html', {'preferences': preferences})

@login_required()
@user_passes_test(teacher_group_required)
def add_preference(request):
    selected_date = request.GET.get('date', datetime.today().strftime('%Y-%m-%d'))
    if request.method == 'POST':
        form = DutyPreferenceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('preference_list')
    else:
        form = DutyPreferenceForm()
    return render(request, 'add_preference.html', {'form': form})

@login_required()
@user_passes_test(teacher_group_required)
def edit_preference(request, pk):
    preference = get_object_or_404(DutyPreference, pk=pk)
    if request.method == 'POST':
        form = DutyPreferenceForm(request.POST, instance=preference)
        if form.is_valid():
            form.save()
            return redirect('preference_list')
    else:
        form = DutyPreferenceForm(instance=preference)
    return render(request, 'add_preference.html', {'form': form})

@login_required()
@user_passes_test(teacher_group_required)
def delete_preference(request, pk):
    preference = get_object_or_404(DutyPreference, pk=pk)
    if request.method == 'POST':
        preference.delete()
        return redirect('preference_list')
    return render(request, 'delete_preference.html', {'preference': preference})

@login_required
@user_passes_test(teacher_group_required)
def duty_history(request):
    user = request.user

    # Ensure the user has a linked teacher profile
    if hasattr(user, 'teacher'):
        teacher = user.teacher
        duty_records = DutyAllotment.objects.filter(teacher=teacher)
    else:
        duty_records = []

    return render(request, 'duty_history.html', {'duty_records': duty_records})
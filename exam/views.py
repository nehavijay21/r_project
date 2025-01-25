from django.shortcuts import render, get_object_or_404, redirect
from .models import Programme
from .forms import ProgramForm
from .models import Room
from .forms import RoomForm


def index(request):
    return render(request, 'index.html')

def manage_programs(request):
    return render(request, 'manage_programs.html')

def manage_rooms(request):
    return render(request, 'manage_rooms.html')

# Add more views as needed


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

from django.shortcuts import get_object_or_404, redirect
from .models import Room

def delete_room(request, pk):
    # Get the room object to delete
    room = get_object_or_404(Room, pk=pk)
    
    if request.method == 'POST':
        room.delete()
        return redirect('room_list')  # Redirect to the room list page after deletion
    
    return render(request, 'delete_room.html', {'room': room})

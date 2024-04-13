from django.shortcuts import render, redirect
from .models import DutySchedule
from .forms import DutyScheduleForm

def add_duty_schedule(request):
    if request.method == 'POST':
        form = DutyScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('display_duty_schedule')
    else:
        form = DutyScheduleForm()
    return render(request, 'app/add_duty_schedule.html', {'form': form})

def display_duty_schedule(request):
    duty_schedule = DutySchedule.objects.all()
    return render(request, 'app/display_duty_schedule.html', {'duty_schedule': duty_schedule})

def update_schedule(request,pk):
#fetching the data of perticular ID
 get_data=DutySchedule.objects.get(id=pk)
 return render(request,'app/update_schedule.html',{'key2':get_data})

def savedata(request,pk):
#  print(request.POST)
 udata=DutySchedule.objects.get(id=pk)
 udata.doctor_name=request.POST['doctor_name']
 udata.day=request.POST['day']
 udata.shift=request.POST['shift']
 udata.save()
 return redirect('display_duty_schedule')
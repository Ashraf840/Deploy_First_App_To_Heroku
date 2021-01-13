from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


# Create your views here.
def studentList(request):
    queryset = Student.objects.all()
    context = {
        'title':'Student List',
        'studentlist':queryset,
    }
    return render(request, 'conMySQLapp/index.html', context)


def studentListCreate(request):
    form = StudentForm()
    
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentlist')

    context = {
        'title':'New Student',
        'header_title':'Create New Student',
        'form_title':'New Student Entry Form',
        'button_name':'Insert',
        'form':form,
    }
    return render(request, 'conMySQLapp/create_edit_student.html', context)



def studentListEdit(request, stdid):
    queryset = Student.objects.get(pk=stdid)
    form = StudentForm(instance=queryset)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=queryset)     # Need to write instance, so that it doen't create any new student entry
        if form.is_valid():
            form.save()
            return redirect('studentlist')


    context = {
        'title':'Edit Student',
        'header_title':'Edit Student',
        'form_title':'Student Edit Form',
        'button_name':'Update',
        'form':form,
        'stdid':stdid,
    }
    return render(request, 'conMySQLapp/create_edit_student.html', context)



def studentListDelete(request, stdid):
    student = Student.objects.get(pk = stdid)
    student.delete()
    return redirect('studentlist')
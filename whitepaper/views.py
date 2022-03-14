from django.shortcuts import render, redirect
from whitepaper.forms import RegistrationForm
from whitepaper.models import Registration

# Create your views here.
def regis(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = RegistrationForm()
    return render(request, 'index.html', {'form':form})

def show(request):  
    registrations = Registration.objects.all()  
    return render(request,"show.html",{'registrations':registrations})  
def edit(request, id):  
    registration = Registration.objects.get(id=id)  
    return render(request,'edit.html', {'registration':registration})  
def update(request, id):  
    registration = Registration.objects.get(id=id)  
    form = RegistrationForm(request.POST, instance = registration)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'registration': registration})  
def destroy(request, id):  
    registration = Registration.objects.get(id=id)  
    registration.delete()  
    return redirect("/show")

from django.shortcuts import render,redirect
from .forms import ContactForm
from .models import ContactDatas
from django.core.mail import send_mail
from django.conf import settings
from django.db.models import Q
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import gspread
from oauth2client.service_account import ServiceAccountCredentials


def admin_page(request):
     if request.method == "POST":
        username=request.POST.get('username')
        pass1=request.POST.get('pass')  
        # print(username,pass1)
        user=authenticate(request,username=username,password=pass1)
        if user is not None and user.is_superuser:
            login(request,user)
            return redirect('admin-page')
        else:
            return render(request,'infoapp/admin-login.html',{'error' : 'Incorrect Details!'})
        # print(username,pass1)
     return render(request,'infoapp/admin-login.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            first = form.cleaned_data['firstname']
            last = form.cleaned_data['lastname']
            phone=form.cleaned_data['phonenumber']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']


            #--------------------------------------------->>>>
            #Google Sheet Append_Data

            scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
            credentials = ServiceAccountCredentials.from_json_keyfile_name('infoapp\key.json', scope)
            gc = gspread.authorize(credentials)
            spreadsheet_name = 'contact_data'
            worksheet_name = 'Sheet1'
            worksheet = gc.open(spreadsheet_name).worksheet(worksheet_name)

            #--------------------------------------------->>>>


            row = [first, last, phone, email, message]
            content= f'Dear {first},\n\nThank you for contacting us. We appreciate your interest and will get back to you as soon as possible.\n\nBest regards,\nGokul.C '
            
            #--------------------------------------------->>>>
            #Send Mail For Replay To User

            send_mail(

                'Thank you for contacting us!',  #Title
                content,                         #Content Of  the Mail 
                'settings.EMAIL_HOST_USER',      #Sender Mail
                [email],                         #Reciver Mail
                fail_silently=False
                )
            #<<<<<<---------------------------------------------

            form.save() #Data Save To Backend 
            worksheet.insert_row(row, index=2) #Data Save To Google Sheet 
            
            return render(request, 'infoapp/main.html',{'message':message})
            
    else:
        form = ContactForm()
    return render(request, 'infoapp/main.html', {'form': form})



@login_required(login_url='login')
def data_list(request):
    search_query = ""
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    employees = ContactDatas.objects.filter(
        Q(firstname__icontains=search_query) | 
        Q(phonenumber__icontains=search_query) |
        Q(email__icontains=search_query)
    )

    context = {
        'employees': employees,
        'search_query': search_query,
    }
    return render(request, 'infoapp/list.html', context)




def edit_data(request, pk):
    employee = ContactDatas.objects.get(id=pk)
    form = ContactForm(instance=employee)

    if request.method == 'POST':
        form = ContactForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('admin-page')

    context = {
        'employee': employee,
        'form': form,
    }
    return render(request, 'infoapp/edit.html', context)


def delete_data(request, pk):
    employee = ContactDatas.objects.get(id=pk)

    if request.method == 'POST':
        employee.delete()
        return redirect('admin-page')

    context = {
        'employee': employee,
    }
    return render(request, 'infoapp/delete.html', context)


def user_logout(request):
    logout(request)
    return redirect('login')

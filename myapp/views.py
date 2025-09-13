
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.views.generic.edit import CreateView

import random
import datetime
from datetime import date  

from myapp.models import Budget, Contact, login, employee_info
from .forms import  EmployeeInfoForm, HotelForm, CompanyForm
# Create your views here.

def deshboard(request):
        text = {'name':'Akram','Course':'Bangla'}
        return render(request,'myapp/home.html',context=text)
    #text = { 'name' : 'Akram', 'Course' : 'Bangla'}
def home(request):
    return render(request,'myapp/home.html')
   
def blogs(request):
        teacher = { 'tname': ['AB', 'BC', 'CA'] }
        return render(request,'myapp/blogs.html', context=teacher)
   
def about(request):
    return render(request,'myapp/about.html')
def production(request):
        year = '2022-23'  
        pyear = 'Boro'
        pyield = 4.75
        year = '2022-23'
        year = '2022-23'
        lenght1 = 'Amer sonar bangala ami tumay balobasi'       
        
        data = { 'y': year,
                'py': pyear, 
                'pyi': pyield,
                'l': lenght1
                }
        return render(request,'myapp/production.html', context=data)



def user_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)  # ✅ Pass both `request` and `user`
            messages.success(request, "Login successful!")
            return redirect("home")  # Redirect to home or another page
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'myapp/login.html')


def add(request):                             
        val1 = int(request.POST['num1'])
        val2 = int(request.POST['num2']) 
        val =  val1+val2
        
        return render(request, 'myapp/test.html', {'Result' : val})
           
def contact(request):
        if request.method=="POST":
          name1 = request.POST['name'] 
          email2 = request.POST['email'] 
          des3 = request.POST['des']    
          values = Contact(name=name1, email=email2,des=des3)       
          values.save()
        
        return render(request,'myapp/contact.html')
   


def welcome(request):
        
        return render(request, 'myapp/welcome.html')

def employee_info1(request):
        
        if request.method =='POST':                
                emId1 = request.POST['em_Id']
                em_Name1 = request.POST['em_Name']
                em_Mobile1 = request.POST['em_Mobile']
                em_Salary1 = request.POST['em_Salary']
                em_Email1 = request.POST['em_Email']               
                em_Birth_Date1 = request.POST['em_Birth_Date']
                em_Desin1 = request.POST['em_Desin']
                em_Join_Date1 = request.POST['em_Join_Date']
                em_Dept1 = request.POST['em_Dept']
                com_Id1 = request.POST['com_Id'] 
                values = employee_info(em_Id=emId1,
                                       em_Name=em_Name1,
                                       em_Mobile=em_Mobile1,
                                       em_Salary=em_Salary1,
                                       em_Email=em_Email1,
                                       em_Birth_Date=em_Birth_Date1,
                                       em_Desin=em_Desin1,
                                       em_Join_Date=em_Join_Date1,
                                       em_Dept=em_Dept1,
                                       com_Id=com_Id1,                                      
                                       )   
                values.save()             
        return render(request,'myapp/employee_info_form.html')        





# Create your views here.


def hotel_image_view(request):
    if request.method == 'POST':
        form = HotelForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = HotelForm()
    return render(request, 'myapp/hotel_image_form.html', {'form': form})


def success(request):
        return HttpResponse('successfully uploaded')


def company_entry(request):
        
        if request.method == 'POST':
                form = CompanyForm(request.POST,)
        form = CompanyForm()        
        return render(request,'myapp/company_entry.html', {'form': form})

def EmployeeInfo(request):
        if request.method == 'POST':
            form = EmployeeInfoForm(request.POST,)
        form = EmployeeInfoForm()         
        
        return render(request,'',{})
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Please login.")
            return redirect('user_login')   # login পেজে রিডাইরেক্ট করবে
    else:
        form = UserCreationForm()
    
    return render(request, 'myapp/register.html', {'form': form})

def forget_password(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if not User.objects.filter(email=email).exists():
            messages.error(request, "No user found with this email!")
            return redirect("forget_password")
        
        # Generate OTP
        otp = random.randint(100000, 999999)
        request.session['reset_otp'] = otp
        request.session['reset_email'] = email
        
        # Send OTP via email
        send_mail(
            "Password Reset OTP",
            f"Your OTP for password reset is: {otp}",
            "noreply@yourwebsite.com",
            [email],
            fail_silently=False,
        )
        
        messages.success(request, "OTP sent to your email. Please check your inbox.")
        return redirect("verify_otp")
    
    return render(request, "myapp/forget_password.html")


# Verify OTP
def verify_otp(request):
    if request.method == "POST":
        input_otp = request.POST.get("otp")
        session_otp = str(request.session.get("reset_otp"))
        
        if input_otp == session_otp:
            messages.success(request, "OTP verified. You can now reset your password.")
            return redirect("reset_password")
        else:
            messages.error(request, "Invalid OTP. Try again!")
            return redirect("verify_otp")
    
    return render(request, "myapp/verify_otp.html")




# Forgot Password
# def forget_password(request):
#     if request.method == "POST":
#         email = request.POST.get("email")
        
#         if not User.objects.filter(email=email).exists():
#             messages.error(request, "No user found with this email!")
#             return redirect("forget_password")
        
#         # Generate OTP
#         otp = random.randint(100000, 999999)
#         request.session['reset_otp'] = otp
#         request.session['reset_email'] = email
        
#         # Send OTP via email
#         send_mail(
#             "Password Reset OTP",
#             f"Your OTP for password reset is: {otp}",
#             "noreply@yourwebsite.com",
#             [email],
#             fail_silently=False,
#         )
        
#         messages.success(request, "OTP sent to your email. Please check your inbox.")
#         return redirect("verify_otp")
    
#     return render(request, "myapp/forget_password.html")

# # Verify OTP and Reset Password
# def verify_otp(request):
#     if request.method == "POST":
#         entered_otp = request.POST.get("otp")
#         saved_otp = request.session.get("reset_otp")
#         email = request.session.get("reset_email")

#         if not saved_otp or str(entered_otp) != str(saved_otp):
#             messages.error(request, "Invalid OTP!")
#             return redirect("verify_otp")

#         request.session["otp_verified"] = True
#         messages.success(request, "OTP verified! You can now reset your password.")
#         return redirect("reset_password")
    
#     return render(request, "myapp/verify_otp.html")

# # Reset Password
def reset_password(request):
    if request.method == "POST":
        if not request.session.get("otp_verified"):
            messages.error(request, "Unauthorized action!")
            return redirect("forget_password")
        
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")
        email = request.session.get("reset_email")
        
        if new_password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("reset_password")
        
        user = User.objects.get(email=email)
        user.set_password(new_password)
        user.save()
        
        # Clear session data
        request.session.pop("reset_otp", None)
        request.session.pop("reset_email", None)
        request.session.pop("otp_verified", None)
        
        messages.success(request, "Password reset successfully! You can now log in.")
        return redirect("login")
    
    return render(request, "myapp/reset_password.html")

from django.shortcuts import render, redirect
from .forms import BudgetForm

def budget_entry(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)  # Use uppercase POST
        if form.is_valid():
            budget = form.save(commit=False) # d;nt save yet
            # increse amount 5%
            budget.amount =  int(budget.amount*1.05)
            budget.save()  # You missed the parentheses
            return redirect('budget_entry')  # Redirect after successful save to prevent resubmission
    else:
        form = BudgetForm()  # Create an empty form for GET requests

    return render(request, 'myapp/budget_entry.html', {'form': form})

def budget_info(request):
    form = Budget.objects.all()
    return render(request, 'myapp/budget_info.html', { 'form' : form })

from django.shortcuts import render, redirect, get_object_or_404
from .models import Budget
from .forms import BudgetForm

# ✅ Edit Budget
def budget_edit(request, pk):
    budget = get_object_or_404(Budget, pk=pk)

    if request.method == 'POST':
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            form.save()
            return redirect('budget_info')  # after saving, go back to the list
    else:
        form = BudgetForm(instance=budget)

    return render(request, 'myapp/budget_edit.html', {'form': form, 'budget': budget})


# ✅ Delete Budget (with confirmation)
def budget_delete(request, pk):
    budget = get_object_or_404(Budget, pk=pk)

    if request.method == 'POST':
        budget.delete()
        return redirect('budget_info')  # after deletion, go back to the list

    # confirmation page
    return render(request, 'myapp/budget_delete.html', {'budget': budget})

from django.shortcuts import render
from django.db.models import Q

def search_budget(request):
    query = request.GET.get('q')  # URL থেকে query string
    if query:
        results = Budget.objects.filter(
            Q(b_id__icontains=query) | Q(subcode__icontains=query) | Q(amount__icontains=query)
        )
    else:
        results = Budget.objects.all()
    
    return render(request, 'myapp/search_budget.html', {'budgets': results})

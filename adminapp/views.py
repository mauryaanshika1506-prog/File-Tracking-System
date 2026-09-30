from django.shortcuts import render, redirect
from django.contrib import messages
from mainapp.models import *
from django.shortcuts import get_object_or_404
# Create your views here.
def admindash(request):
    if 'adminid' not in request.session:
        messages.error(request, "Please login first")
        return redirect('adminlogin')
    adminid = request.session.get('adminid')
    total_files=File.objects.count()
    pending_files=File.objects.exclude(status="CLOSED").count()
    total_employees=Employee.objects.count()
    total_departments=Department.objects.count()
    context = {
       'adminid' : adminid,
       'total_files' : total_files,
       'pending_files' : pending_files,
       'total_employees' : total_employees,
       'total_departments' : total_departments,
    }
    return render(request, "admindash.html", context)

def adminlogout(request):
    if 'adminid' in request.session:
        del request.session['adminid']
        messages.success(request, "logged out successfully")
        return redirect("adminlogin")
    else:
        return redirect("adminlogin")

def adddept(request):
    if 'adminid' not in request.session:
        messages.error(request, "Please login first")
        return redirect('adminlogin')
    adminid = request.session.get('adminid')
    context = {
       'adminid' : adminid,
    }
    if request.method == "POST":
        dept_name = request.POST.get('dept_name')
        if Department.objects.filter(dept_name=dept_name):
            messages.warning(request, "This department already exists")
            return redirect("adddept")
        dep = Department(dept_name=dept_name)
        dep.save()
        messages.success(request, "Department added successfully")
        return redirect("viewdept")
    return render(request, "adddept.html", context)

def viewdept(request):
    if 'adminid' not in request.session:
        messages.error(request, "Please login first")
        return redirect('adminlogin')
    adminid = request.session.get('adminid')
    depts= Department.objects.all()
    context = {
       'adminid' : adminid,
       'depts' : depts,
    }
    return render(request, "viewdept.html", context)

def addemp(request):
    if 'adminid' not in request.session:
        messages.error(request, "Please login first")
        return redirect('adminlogin')
    adminid = request.session.get('adminid')
    depts= Department.objects.all()
    context = {
       'adminid' : adminid,
       'depts' : depts,
    }
    if request.method == "POST":
        empid = request.POST.get('empid')
        name = request.POST.get('name')
        contactno = request.POST.get('contactno')
        email = request.POST.get('email')
        designation = request.POST.get('designation')
        dept_id = request.POST.get('dept_id')
        dept = Department.objects.get(id=dept_id)
        if LoginInfo.objects.filter(username=email):
            messages.warning(request, "This email is already registered")
            return redirect("addemp")
        log = LoginInfo.objects.create(usertype="employee", username=email, password="12345678" )
        emp = Employee.objects.create(log=log, empid=empid, name=name, contactno=contactno, email=email, designation=designation, department=dept)
        messages.success(request, "Employee added successfully")
        return redirect("viewemp")
    return render(request, "addemp.html", context)

def viewemp(request):
    if 'adminid' not in request.session:
        messages.error(request, "Please login first")
        return redirect('adminlogin')
    adminid = request.session.get('adminid')
    depts = Department.objects.all()
    emp1 = Employee.objects.all()
    context = {
       'adminid' : adminid,
        'depts' : depts,
        'emp1' : emp1,
          }
    return render(request, "viewemp.html", context)

def changepass(request):
    if 'adminid' not in request.session:
        messages.error(request, "Please login first")
        return redirect('adminlogin')
    adminid = request.session.get('adminid')
    context = {
       'adminid' : adminid,
     }
    if request.method == "POST":
        oldpwd = request.POST.get("oldpwd")
        newpwd = request.POST.get("newpwd")
        cnfpwd = request.POST.get("cnfpwd")
        admin = LoginInfo.objects.get(username=adminid)
        if newpwd != cnfpwd:
            messages.warning(request, "Enter same same password")
            return redirect("changepass")
        if oldpwd != admin.password:
            messages.warning(request, "Old password is incorrect")
            return redirect("changepass")
        if newpwd == admin.password:
            messages.warning(request, "you cannot set privious password")
            return redirect("changepass")
        admin.password = newpwd
        admin.save()
        messages.success(request, "password change successfully")
        return redirect("changepass")
    return render(request, "changepass.html", context)

def deldept(request,did):
    if'adminid' not in request.session:
        messages.error(request,"plese login first")
        return redirect('admin_login')
    if Department.objects.filter(id=did):
        Department.objects.get(id=did).delete()
        messages.success(request,"Department deleted succesfully")
        return redirect("viewdept")
    else:
        return redirect("viewdept")

def allfiles(request):
    if'adminid' not in request.session:
        messages.error(request,"plese login first")
        return redirect('admin_login')
    adminid = request.session.get('adminid')
    files=File.objects.all()
    context={
        'adminid':adminid,
        'files':files,
    }
    
    return render(request,"allfiles.html",context)

def updateattachment(request, id):

    if 'adminid' not in request.session:
        return redirect('adminlogin')

    file = get_object_or_404(File, id=id)

    if request.method == "POST":
        attachment = request.FILES.get("file_attachment")

        if attachment:
            file.file_attachment = attachment
            file.save()

            messages.success(
                request,
                "File attachment updated successfully"
            )

        return redirect('viewfiles')

    return render(
        request,
        "updateattachment.html",
        {"file": file}
    )


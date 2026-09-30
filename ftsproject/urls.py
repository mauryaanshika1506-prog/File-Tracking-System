"""
URL configuration for ftsproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainapp import views
from adminapp.views import *
from empapp.views import *

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('adminlogin/',views.adminlogin,name='adminlogin'),
    path('userlogin/',views.userlogin,name='userlogin'),
    #adminapp urls
    path('admindash/', admindash, name="admindash"),
    path('adminlogout/', adminlogout, name="adminlogout"),
    path('adddept/', adddept, name="adddept"),
    path('viewdept/', viewdept, name="viewdept"),
    path('addemp/', addemp, name="addemp"),
    path('viewemp/', viewemp, name="viewemp"),
    path('changepass/', changepass, name="changepass"),
    path('allfiles', allfiles, name="allfiles"),
    path('deldept/<did>', deldept, name="deldept"),
    path('updateattachment/<int:id>/', updateattachment, name='updateattachment'),
    # empapp urls
    path('empdash/', empdash, name="empdash"),
    path('emplogout/', emplogout, name="emplogout"),
    path('viewprofile/', viewprofile, name="viewprofile"),
    path('updateprofile/', updateprofile, name="updateprofile"),
    path('initiatefile/', initiatefile, name="initiatefile"),
    path('viewfiles/', viewfiles, name="viewfiles"),
    path('recievedfiles/', recievedfiles, name="recievedfiles"),
    path('filedetails/<fid>', filedetails, name="filedetails"),
    path('closefile/<fid>', closefile, name="closefile"),
    path('empchangepass/', empchangepass, name="empchangepass"),
    path('employeetrackfile/', employeetrackfile, name='employeetrackfile'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.shortcuts import render,redirect
from core.models import *

# Create your views here.
def myhome(request):
    return render(request, "Home.html")

def abc (request):
    return render(request,"abc.html")

def create(request):
    if request.method == "POST":
        f_name = request.POST.get("firstName")
        l_name = request.POST.get("lastName")
        p_num = request.POST.get("phone")
        e_mail = request.POST.get("email")
        text= request.POST.get("message")
        print(f_name,l_name,p_num,e_mail,text)
        data = UserData.objects.create(first_name = f_name,last_name=l_name, phone = p_num,email= e_mail ,  message = text)
        data.save()
        if f_name:
            return redirect('View')      
    return render(request, "Create.html")

def forview(request):
    user_data = UserData.objects.all()
    context = {'data' : user_data }
    print(user_data)
    return render(request,"view.html",context)

def update(request,id):

    data = UserData.objects.get(id = id)
    name = "Anup"
    context = {
            'updatedata' : data , 'name' : name
        }
    if request.method == "POST":
         # id = database , id = Button ma pass garako id
        print(data.first_name,data.last_name,data.phone,data.email,data.message)
        f_name = request.POST.get("firstName")
        l_name = request.POST.get("lastName")
        p_num = request.POST.get("phone")
        e_mail = request.POST.get("email")
        text= request.POST.get("message")
        print(f_name,l_name,p_num,e_mail,text)
        data.first_name = f_name
        data.last_name = l_name
        data.phone = p_num
        data.email = e_mail
        data.message = text
        data.save()
        
        return redirect("View")

    return render(request,"updatevalue.html",context)

def delete(request,id):
    todelete = UserData.objects.get(id = id)
    todelete.delete()
    return redirect("View")

def forupdatevalue(request):
    return render(request,"updatevalue.html")

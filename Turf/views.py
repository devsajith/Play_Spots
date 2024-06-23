from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
# Create your views here.
from django.views.generic import TemplateView

# from Turf.models import

# Create your views here.
from django.views.generic import TemplateView

from Turf.models import UserType, Userreg, Ownerreg


class IndexView(TemplateView):
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password= request.POST['password']
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request,user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "user":
                    return redirect('/user')
                else:
                    return redirect('/owner')
            else:
                return render(request,'index.html',{'message':" User Account Not Authenticated"})
        else:
            return render(request,'index.html',{'message':"Invalid Username or Password"})

class CategoryView(TemplateView):
    template_name = 'category.html'

    def post(self, request,*args,**kwargs):
        category = request.POST['category']
        if category=='1':
            return redirect('/userreg')
        else:
            return redirect('/ownerreg')


class OwnerReg(TemplateView):
    template_name = 'owner_reg.html'

    def post(self, request,*args,**kwargs):
        fullname = request.POST['c_name']
        con = request.POST['p_number']
        ad = request.POST['coad']
        oad = request.POST['oad']
        email = request.POST['email']
        password = request.POST['pass']

        try:
             user = User.objects.create_user(username=email,password=password,first_name=fullname,email=email,last_name=0)
             user.save()
             reg = Ownerreg()
             reg.user = user
             reg.contact = con
             reg.owner_addr = oad
             reg.address = ad
             reg.save()
             usertype = UserType()
             usertype.user = user
             usertype.type = "owner"
             usertype.save()
             messages = "Register Successfully"
             return render(request, 'index.html', {'message': messages})
        except:
             messages = "Email address already used!.."
             return render(request,'index.html',{'message':messages})



class UserReg(TemplateView):
    template_name = 'user_reg.html'

    def post(self, request, *args, **kwargs):
        fullname = request.POST['name']
        con = request.POST['phone']
        ad = request.POST['addre']
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.create_user(username=email, password=password, first_name=fullname, email=email,
                                            last_name=0)
            user.save()
            reg = Userreg()
            reg.user = user
            reg.contact = con
            reg.address = ad
            reg.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "user"
            usertype.save()
            messages = "Register Successfully"
            return render(request, 'index.html', {'message': messages})
        except:
            messages = "Email address already used!.."
            return render(request, 'index.html', {'message': messages})
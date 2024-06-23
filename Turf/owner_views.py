from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# from Turf.models import HR_Reg, Applicant_Reg, Employee, HrReport, AddWork
from Turf.models import Ownerreg, Turf, BookTurf, Package


class IndexView(TemplateView):
    template_name = 'owner/owner_index.html'

class ManageTurf(LoginRequiredMixin,TemplateView):
    template_name = 'owner/manage_turf.html'
    login_url = '/'



class AddTurf(LoginRequiredMixin,TemplateView):
    template_name = 'owner/add_turf.html'
    login_url = '/'

    def post(self, request,*args,**kwargs):
        fullname = request.POST['name']
        description = request.POST['description']
        location = request.POST['location']
        price = request.POST['price']
        image1 = request.FILES['image1']
        image2 = request.FILES['image2']
        image3 = request.FILES['image3']
        fec = request.POST['fec']

        ow = Ownerreg.objects.get(user_id=self.request.user.id)

        t = Turf()
        t.owner = ow
        t.name = fullname
        t.descri = description
        t.location = location
        t.price = price
        t.image1 = image1
        t.image2 = image2
        t.image3 = image3
        t.facility = fec
        t.status = 'Post'
        t.save()

        messages = "Added Successfully"
        return render(request,'owner/owner_index.html',{'message':messages})




class ViewTurf(LoginRequiredMixin,TemplateView):
    template_name = 'owner/view_turf.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ViewTurf,self).get_context_data(**kwargs)
        ow = Ownerreg.objects.get(user_id=self.request.user.id)
        p = Turf.objects.filter(owner_id=ow,status='Added')
        context['p'] = p
        return context

class UpdateTurf(LoginRequiredMixin,TemplateView):
    template_name = 'owner/update_turf.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(UpdateTurf,self).get_context_data(**kwargs)
        t = self.request.GET['id']
        p = Turf.objects.get(pk=t)
        context['p'] = p
        return context

    def post(self, request,*args,**kwargs):
        fullname = request.POST['name']
        description = request.POST['description']
        location = request.POST['location']
        price = request.POST['price']
        fec = request.POST['fec']
        id = request.POST['id']



        t = Turf.objects.get(pk=id)

        t.name = fullname
        t.descri = description
        t.location = location
        t.price = price
        t.facility = fec
        t.save()

        messages = "Updated Successfully"
        return render(request,'owner/owner_index.html',{'message':messages})

class DeleteTurf(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        Turf.objects.get(pk=id).delete()
        return render(request,'owner/owner_index.html',{'message':"Turf Deleted"})


class ViewTurfBooking(TemplateView):
    template_name = 'owner/view_turf_booking.html'

    def get_context_data(self, **kwargs):
        context = super(ViewTurfBooking,self).get_context_data(**kwargs)
        u = Ownerreg.objects.get(user_id=self.request.user.id)
        b = BookTurf.objects.filter(turf__owner_id=u)
        context['b'] = b
        return context

class AcceptTurf(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        s = BookTurf.objects.get(pk=id)
        s.status = 'Accepted'
        s.save()
        return render(request,'owner/owner_index.html',{'message':"Booking Accepted"})

class RejectTurf(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        s = BookTurf.objects.get(pk=id)
        s.status = 'Reject'
        s.save()
        return render(request,'owner/owner_index.html',{'message':"Booking Reject"})


class AddPackage(TemplateView):
    template_name = 'owner/add_package.html'

    def get_context_data(self, **kwargs):
        context = super(AddPackage,self).get_context_data(**kwargs)
        id= self.request.GET['id']
        context['id'] = id
        return context

    def post(self, request,*args,**kwargs):
        description = request.POST['description']
        tur = request.POST['tur']
        fdate = request.POST['fdate']
        tdate = request.POST['tdate']
        disc = request.POST['disc']




        t = Turf.objects.get(pk=tur)
        pk = Package.objects.filter(turf=t).count()
        if pk >0:
            messages = "Package Already Added"
            return render(request, 'owner/owner_index.html', {'message': messages})
        else:

            p = Package()
            p.tdate = tdate
            p.fdate = fdate
            p.discount = disc
            p.pack = description
            p.turf = t

            p.save()

            messages = "Added Successfully"
            return render(request,'owner/owner_index.html',{'message':messages})

class ViewPackage(TemplateView):
    template_name = 'owner/view_package.html'

    def get_context_data(self, **kwargs):
        context = super(ViewPackage,self).get_context_data(**kwargs)
        id= self.request.GET['id']
        pk = Package.objects.filter(turf=id)
        context['b'] = pk
        return context

class  DeletePack(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        s = Package.objects.get(pk=id).delete()

        return render(request, 'owner/owner_index.html', {'message': "Package Deleted."})
import datetime
import json
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

# from Turf.models import HR_Reg, Applicant_Reg, Employee, HrReport, AddWork
from Turf.models import Userreg, Turf, BookTurf, Feedback, Package
from datetime import date

class IndexView(LoginRequiredMixin,TemplateView):
    template_name = 'user/user_index.html'
    login_url = '/'


class ViewTurf(LoginRequiredMixin,TemplateView):
    template_name = 'user/view_turf.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ViewTurf,self).get_context_data(**kwargs)
        s = Turf.objects.filter(status='Added')
        context['s'] = s
        return context

class TurfDetails(LoginRequiredMixin,TemplateView):
    template_name = 'user/turf_details.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(TurfDetails,self).get_context_data(**kwargs)
        id = self.request.GET['id']
        s = Turf.objects.get(pk=id)
        try:
            p = Package.objects.get(turf=s)

            tdt = p.tdate

            fdt = p.fdate
            today = datetime.datetime.today()
            # date_to = datetime.datetime.strptime(today, '%Y-%m-%d')
            date_t = datetime.datetime.strptime(tdt, '%Y-%m-%d')
            date_f = datetime.datetime.strptime(fdt, '%Y-%m-%d')
            if date_f <= today <= date_t:
                context['p'] = p
            else:
                pass
        except:
            pass
        context['s'] = s
        return context

class BookTurfs(LoginRequiredMixin,TemplateView):
    template_name = 'user/book_turf.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(BookTurfs,self).get_context_data(**kwargs)
        try:
            dis = self.request.GET['dis']
            pack = self.request.GET['pack']
            tprice = self.request.GET['tprice']
            id = self.request.GET['tid']
            tp = int(tprice)-((int(tprice)*int(dis))/100)
            print(tp)
            context['p'] = tp
            context['pack'] = pack
            context['id'] = id
        except:
            tprice = self.request.GET['tprice']
            id = self.request.GET['tid']
            context['pack'] = ""
            context['id'] = id
            context['p'] = tprice
        return context

    def post(self, request,*args,**kwargs):

        pack = request.POST['pck']

        tf = request.POST['tf']
        bodate = request.POST['bodate']

        uti = request.POST['ti']
        to = request.POST['to']
        no = request.POST['no']
        forw = request.POST['forw']

        ufti = datetime.datetime.strptime(uti, '%I:%M')
        utfis = ufti.time()



        s = Turf.objects.get(pk=tf)
        u = Userreg.objects.get(user_id=self.request.user.id)

        std = BookTurf.objects.filter(b_date=bodate,time=utfis,turf=s,status__icontains='Booked').count()
        stds = BookTurf.objects.filter(b_date=bodate,time=utfis,turf=s,status__icontains='Accepted').count()
        if std >0 or stds >0:
            # std = BookTurf.objects.filter(b_date=bodate)
            #
            # for std in std:
            #     tti = std.time
            #     tnoh = std.noh
            #     fti = datetime.datetime.strptime(tti, '%I:%M')
            #     ftit = fti.time()
            #     s = fti + datetime.timedelta(hours=int(tnoh))
            #     st = s.time()
            #     sti = datetime.datetime.strptime(st, '%I:%M')
            #     stis = sti.time()
            #
            #
            #     if ftit <= utfis <= stis:
            messages = "This Time Period Is Already Booked.Please Choose Another.."
            return render(request, 'user/user_index.html', {'message': messages})
            # t = BookTurf()
            #
            # t.time = utfis
            # t.total = to
            # t.turf = s
            # t.forwhat = forw
            # t.user = u
            # t.noh = no
            # t.b_date = bodate
            # t.status = 'Booked'
            # t.save()
            # messages = "Booke Successfully"
            # return render(request, 'user/user_index.html', {'message': messages})

        else:
            t = BookTurf()

            t.time = utfis
            t.total = to
            t.turf = s
            t.forwhat = forw
            t.user = u
            t.noh = no
            t.b_date = bodate
            if pack == "":

                t.pack = "Not Package Available"
            else:
                t.pack = pack
            t.status = 'Booked'
            t.save()
            messages = "Booked Successfully"
            return render(request, 'user/user_index.html', {'message': messages})

class ViewTurfBooking(LoginRequiredMixin,TemplateView):
    template_name = 'user/view_turf_booking.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ViewTurfBooking,self).get_context_data(**kwargs)
        u = Userreg.objects.get(user_id=self.request.user.id)
        b = BookTurf.objects.filter(user_id=u)
        context['b'] = b
        return context

class AddFeedback(LoginRequiredMixin,TemplateView):
    template_name = 'user/feedback.html'
    login_url = '/'

    def post(self, request,*args,**kwargs):

        feed = request.POST['feed']

        u = Userreg.objects.get(user_id=self.request.user.id)
        f = Feedback()

        f.feed = feed
        f.user = u
        f.save()
        messages = "Feedback Added Successfully"
        return render(request, 'user/user_index.html', {'message': messages})

class CancelBooking(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET.get('book_id')
        print(id)
        today = datetime.date.today()
        b = BookTurf.objects.get(pk=id)
        bdate = b.b_date
        # sd_obj = datetime.datetime.strptime(today, '%Y-%m-%d')
        fd_obj = datetime.datetime.strptime(bdate, '%Y-%m-%d')
        fd_obj_minus = fd_obj - datetime.timedelta(days=3)
        minus = fd_obj_minus.date()
        if today < minus:
            total = b.total
            per = (int(total)/10)*3
            gt = int(total)-int(per)

            b.status = 'Cancel'
            b.total = gt
            b.save()
            dict = {'name': 'true'}
            sorted_string = json.dumps(dict)
            # print(sorted_string)
            print("true")
            return JsonResponse(sorted_string, safe=False)

        else:
            dict = {'name': 'false'}
            sorted_string = json.dumps(dict)
            # print(sorted_string)
            print("false")
            return JsonResponse(sorted_string, safe=False)


        # return redirect(request.META['HTTP_REFERER'])
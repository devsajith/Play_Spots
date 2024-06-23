from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# from Turf.models import HR_Reg, Applicant_Reg, Employee, HrReport, AddWork
from Turf.models import Ownerreg, Userreg, Turf, Feedback


class IndexView(LoginRequiredMixin,TemplateView):
    template_name = 'admin/admin_index.html'
    login_url = '/'

class ManageOwner(LoginRequiredMixin,TemplateView):
    template_name = 'admin/manage_owner.html'
    login_url = '/'

class RejectView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='0'
        user.is_active='0'
        user.save()
        return render(request,'admin/admin_index.html',{'message':"Account Removed"})

class ApproveView(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        user = User.objects.get(pk=id)
        user.last_name='1'

        user.save()
        return render(request,'admin/admin_index.html',{'message':"Account Activated"})


class ApproveOwner(LoginRequiredMixin,TemplateView):
    template_name = 'admin/approve_owner.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ApproveOwner,self).get_context_data(**kwargs)
        p = Ownerreg.objects.filter(user__last_name='0',user__is_staff='0')

        context['p'] = p

        return context

class ViewOwner(LoginRequiredMixin,TemplateView):
    template_name = 'admin/view_owner.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ViewOwner,self).get_context_data(**kwargs)
        p = Ownerreg.objects.filter(user__last_name='1',user__is_staff='0')

        context['p'] = p

        return context

class ManageUser(LoginRequiredMixin,TemplateView):
    template_name = 'admin/manage_user.html'
    login_url = '/'

class ApproveUser(LoginRequiredMixin,TemplateView):
    template_name = 'admin/approve_user.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ApproveUser,self).get_context_data(**kwargs)
        p = Userreg.objects.filter(user__last_name='0',user__is_staff='0')

        context['p'] = p

        return context

class ViewUser(LoginRequiredMixin,TemplateView):
    template_name = 'admin/view_user.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ViewUser,self).get_context_data(**kwargs)
        p = Userreg.objects.filter(user__last_name='1',user__is_staff='0')

        context['p'] = p

        return context




class ManageTurf(LoginRequiredMixin,TemplateView):
    template_name = 'admin/manage_turf.html'
    login_url = '/'


class NewTurf(LoginRequiredMixin,TemplateView):
    template_name = 'admin/new_turf.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(NewTurf,self).get_context_data(**kwargs)
        p = Turf.objects.filter(status='Post')
        context['p'] = p
        return context

class ApproveTurf(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        t = Turf.objects.get(pk=id)
        t.status = 'Added'

        t.save()
        return render(request,'admin/admin_index.html',{'message':"Turf Added..."})

class DisApproveTurf(View):
    def dispatch(self, request, *args, **kwargs):
        id = request.GET['id']
        t = Turf.objects.get(pk=id)
        t.status = 'Reject'

        t.save()
        return render(request,'admin/admin_index.html',{'message':"Turf Rejected..."})

class ViewTurf(LoginRequiredMixin,TemplateView):
    template_name = 'admin/view_turf.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ViewTurf,self).get_context_data(**kwargs)
        p = Turf.objects.filter(status='Added')
        context['p'] = p
        return context





class ViewFeedback(LoginRequiredMixin,TemplateView):
    template_name = 'admin/feedback.html'
    login_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ViewFeedback,self).get_context_data(**kwargs)
        p = Feedback.objects.all()
        context['p'] = p

        return context
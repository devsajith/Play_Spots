from django.urls import path

from Turf.owner_views import IndexView, ManageTurf, AddTurf, ViewTurf, UpdateTurf, \
    DeleteTurf, \
    AcceptTurf, RejectTurf, ViewTurfBooking, AddPackage, ViewPackage, DeletePack
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('',IndexView.as_view()),
    path('ManageTurf',ManageTurf.as_view()),

    path('AddTurf',AddTurf.as_view()),
    path('ViewTurf',ViewTurf.as_view()),
    path('UpdateTurf',UpdateTurf.as_view()),
    path('DeleteTurf',DeleteTurf.as_view()),

    path('AddPackage',AddPackage.as_view()),
    path('ViewPackage',ViewPackage.as_view()),
    path('DeletePack',DeletePack.as_view()),



    path('ViewTurfBooking',ViewTurfBooking.as_view()),
    path('AcceptTurf',AcceptTurf.as_view()),
    path('RejectTurf',RejectTurf.as_view()),





    path('logout/', auth_views.LogoutView.as_view(
        next_page='/'
        ),
        name='logout'
    ),


]
def urls():
      return urlpatterns,'owner','owner'
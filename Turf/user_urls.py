from django.urls import path

from Turf.user_views import IndexView, ViewTurf, \
    TurfDetails, BookTurfs, ViewTurfBooking, AddFeedback, CancelBooking
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('',IndexView.as_view()),

    path('AddFeedback',AddFeedback.as_view()),

    path('ViewTurf',ViewTurf.as_view()),
    path('TurfDetails',TurfDetails.as_view()),
    path('BookTurf',BookTurfs.as_view()),
    path('ViewTurfBooking',ViewTurfBooking.as_view()),
    path('CancelBooking',CancelBooking.as_view()),


    path('logout/', auth_views.LogoutView.as_view(
        next_page='/'
        ),
        name='logout'
    ),


]
def urls():
      return urlpatterns,'user','user'
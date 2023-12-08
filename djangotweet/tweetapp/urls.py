
from django.urls import path
from . import views
app_name = 'tweetapp'

urlpatterns = [
    path('',views.listtweet,name='listtweet'),
    path('addtweet/',views.addtweet,name='addtweet'),
    path("addtweetbyform/",views.addtweetbyform,name='addtweetbyform'),
    path('singup/',views.SingUpView.as_view(),name="singup"),
    path("deletetweet/<int:id>",views.deletetweet,name="deletetweet"),
]

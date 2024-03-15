from django.urls import path
from .views import *

app_name ='main'


urlpatterns = [
    path('', Home.as_view(), name = 'home'),
    path('projcreate/', ProjectList.as_view(), name= 'project'),
    path('taskcreate/', TaskList.as_view(), name= 'task'),
    path('projupdate/<str:pk>/', ProjectUpdate.as_view(), name= 'projupdate'),
    path('taskupdate/<str:pk>/', TaskUpdate.as_view(), name= 'taskupdate'),
    path('projdelete/<str:pk>/', ProjectDelete.as_view(), name= 'projdelete'),
    path('taskdelete/<str:pk>/', TaskDelete.as_view(), name= 'taskdelete'),
]
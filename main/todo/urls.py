
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='home'),
    path('create_todo/',views.create_todo),
    path('clear_todo/<int:todo_id>/',views.clear_todo),

]





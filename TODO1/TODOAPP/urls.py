from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.fun1,name='fun1'),
    path('delete/<int:studyid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.Studylistview.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.StudyDetailview.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.StudyUpdateView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.StudydeleteView.as_view(),name='cbvdelete'),
   # path('details',views.details,name='details')
     ]

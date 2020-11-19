from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('index',views.index,name='index'),
    path('register',views.register,name='register'),
    path('fundinputpage',views.fundinputpage,name='fundinputpage'),
    path('login',views.login,name='login'),
    path('adminportal',views.adminportal,name='adminportal'),
    path('empreg',views.empreg,name='empreg'),
    path('filtrationunit',views.filtrationunit,name='filtrationunit'),
    path('quality',views.quality,name='quality'),
    path('sanction',views.sanction,name='sanction'),
    path('villagereg',views.villagereg,name='villagereg'),
    path('pipeline',views.pipeline,name='pipeline'),
    path('watersourcereg',views.watersourcereg,name='watersourcereg'),
    path('insertvillage',views.insertvillage,name='insertvillage'),
    path('empinsert',views.employeereg,name='employeereg'),
    path('insertfiltration',views.insertfiltration,name='insertfiltration'),
    path('insertquality',views.insertquality,name='insertquality'),
    path('insertsanction',views.insertsanction,name='insertsanction'),
    path('insertpipe',views.insertpipe,name='insertpipe'),
    path('insertsource',views.insertsource,name='insertsource'),
    path('userreg',views.userreg,name='userreg'),
    path('userlogin',views.userlogin,name='userlogin'),
    path('reqwatercon',views.reqwatercon,name='reqwatercon'),
    path('reqihhl',views.reqihhl,name='reqihhl'),
    path('funding',views.fundretrieve,name='funding'),
    path('newwaterconreq',views.newwaterconreq,name='newwaterconreq'),
    path('newihhlcon',views.newihhlcon,name='newihhlcon'),
    path('fundretrieve',views.fundretrieve,name='fundretrieve'),
    path('insertfund', views.insertfund, name='insertfund'),
    path('waterrevenueinput',views.waterrevenueinput,name='waterrevenueinput'),
    path('waterrevenueretrieve',views.waterrevenueretrieve,name='waterrevenueretrieve'),
    path('insertwaterrevenue',views.insertwaterrevenue,name='insertwaterrevenue'),
    path('registerihhl',views.registerihhl,name='registerihhl'),
    path('insertihhl',views.insertihhl,name='insertihhl'),
    path('villageoutput',views.villageoutput,name='villageoutput')

]
from django.shortcuts import render
from eapp.models import emod
from django.db.models import Sum
from datetime import date,datetime
# Create your views here.
def index(request):
    if request.method == 'GET':
        p = emod.objects.aggregate(Sum('amt'))['amt__sum']
        tot = emod.objects.aggregate(Sum('Total_amount'))['Total_amount__sum']
        s= emod.objects.all()
        amt=[int(obj.amt) for obj in s]
       
        date=[int(obj.date.strftime("%Y%m%d")) for obj in s]
        
        

        bal = tot-p
        
        
        

    return render(request,'eapp/index.html',{'p':p,'bal':bal,'tot':tot,'amt':amt,'date':date,'s':s})

def mon(request):
    exp=''
    ex=''
    asum=''
    aspt=''
    at=''
    ao=''
    if request.method=='POST':
        start_date = request.POST['sdate']
        end_date = request.POST['edate']
        exp = emod.objects.filter(date__range=[start_date,end_date]).aggregate(Sum('Total_amount'))['Total_amount__sum']
        ex = emod.objects.filter(date__range=[start_date,end_date]).values()
        asum=emod.objects.filter(date__range=[start_date,end_date]).aggregate(Sum('amt'))['amt__sum']
        aspt=exp-asum
        at = emod.objects.filter(date__range=[start_date,end_date]).aggregate(Sum('amt_taken'))['amt_taken__sum']
        ao = at-asum

    return render(request,'eapp/month.html',{'exp':exp,'ex':ex,'asum':asum,'aspt':aspt,'at':at,'ao':ao})
   
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django import forms
from .models import JSamajik, JPardes, JEducation, JMedical, Any, DataLogin, Daan


# Create your views here.


def index(request):
    return render(request, 'index.html')


def submit(request):
    return render(request, 'thanks.html')


def educational(request):
    if request.method == "POST" or request.method == "FILES":
        # Educational
        JEName_First = request.POST.get('JEName_First', '')
        JEName_Last = request.POST.get('JEName_Last', '')
        JEMob_num = request.POST.get('JEMob_num', '')
        J1_Name_First = request.POST.get('J1_Name_First', '')
        J1_Name_Last = request.POST.get('J1_Name_Last', '')
        J1_Standard = request.POST.get('J1_Standard', '')
        J1_Fees = request.POST.get('J1_Fees', '')
        J1_Paidfees = request.POST.get('J1_Paidfees', '')
        J1_Paiddate = request.POST.get('J1_Paiddate')
        J1_Rempaidfees = request.POST.get('J1_Rempaidfees', '')
        J1_Receipt = request.FILES.get('J1_Receipt', '')
        j1text = request.POST.get('j1text', '')
        JEEmail = request.POST.get('JEEmail', '')
        educational = JEducation(J1_Name_First=J1_Name_First, J1_Name_Last=J1_Name_Last, J1_Standard=J1_Standard,
                                 J1_Fees=J1_Fees, J1_Paidfees=J1_Paidfees, J1_Paiddate=J1_Paiddate,
                                 J1_Rempaidfees=J1_Rempaidfees, J1_Receipt=J1_Receipt, j1text=j1text,
                                 JEName_First=JEName_First, JEName_Last=JEName_Last, JEMob_num=JEMob_num,
                                 JEEmail=JEEmail)
        educational.save()
        eid = educational.education_key
        thank = True
        return render(request, 'educational.html', {'thank': thank, 'eid': eid})
    return render(request, 'educational.html')


def medical(request):
    if request.method == "POST" or request.method == "FILES":
        # Medical
        JMName_First = request.POST.get('JMName_First', '')
        JMName_Last = request.POST.get('JMName_Last', '')
        JMMob_num = request.POST.get('JMMob_num', '')
        J2_Name_First = request.POST.get('J2_Name_First', '')
        J2_Name_Last = request.POST.get('J2_Name_Last', '')
        J2_HospiName = request.POST.get('J2_HospiName', '')
        J2_DocName = request.POST.get('J2_DocName', '')
        J2_Cost = request.POST.get('J2_Cost', '')
        J2_Receipt = request.FILES.get('J2_Receipt', '')
        j2text = request.POST.get('j2text', '')
        JMEmail = request.POST.get('JMEmail', '')
        medical = JMedical(J2_Name_First=J2_Name_First, J2_Name_Last=J2_Name_Last, J2_HospiName=J2_HospiName,
                           J2_DocName=J2_DocName, J2_Cost=J2_Cost, J2_Receipt=J2_Receipt, j2text=j2text,
                           JMName_First=JMName_First, JMName_Last=JMName_Last, JMMob_num=JMMob_num,
                           JMEmail=JMEmail)
        medical.save()
        mid = medical.medical_key
        thank = True
        return render(request, 'medical.html', {'thank': thank, 'eid': mid})
    return render(request, 'medical.html')


def samajik(request):
    if request.method == "POST" or request.method == "FILES":
        # Samajik
        JSName_First = request.POST.get('JSName_First', '')
        JSName_Last = request.POST.get('JSName_Last', '')
        JSMob_num = request.POST.get('JSMob_num', '')
        j3text = request.POST.get('j3text', '')
        J3_Cost = request.POST.get('J3_Cost')
        JSEmail = request.POST.get('JSEmail', '')
        samajik = JSamajik(j3text=j3text, J3_Cost=J3_Cost, JSName_First=JSName_First, JSName_Last=JSName_Last,
                           JSMob_num=JSMob_num, JSEmail=JSEmail)
        samajik.save()
        thank = True
        sid = samajik.samajik_key
        return render(request, 'samajik.html', {'thank': thank, 'eid': sid})

    return render(request, 'samajik.html')


def pardes(request):
    if request.method == "POST" or request.method == "FILES":
        JPName_First = request.POST.get('JPName_First', '')
        JPName_Last = request.POST.get('JPName_Last', '')
        JPMob_num = request.POST.get('JPMob_num', '')
        J4_Name_First = request.POST.get('J4_Name_First', '')
        J4_Name_Last = request.POST.get('J4_Name_Last', '')
        j4text = request.POST.get('j4text', '')
        J4_muddat = request.POST.get('J4_muddat', '')
        J4_Cost = request.POST.get('J4_Cost', '')
        JPEmail = request.POST.get('JPEmail', '')
        pardes = JPardes(J4_Name_First=J4_Name_First, J4_Name_Last=J4_Name_Last, j4text=j4text, J4_muddat=J4_muddat,
                         J4_Cost=J4_Cost, JPName_First=JPName_First, JPName_Last=JPName_Last, JPMob_num=JPMob_num,
                         JPEmail=JPEmail)
        pardes.save()
        pid = pardes.pardes_key
        thank = True
        return render(request, 'pardes.html', {'thank': thank, 'eid': pid})

    return render(request, 'pardes.html')


def any(request):
    if request.method == "POST" or request.method == "FILES":
        JAName_First = request.POST.get('JAName_First', '')
        JAName_Last = request.POST.get('JAName_Last', '')
        JAMob_num = request.POST.get('JAMob_num', '')
        j5text = request.POST.get('j5text', '')
        J5_Cost = request.POST.get('J5_Cost', '')
        JAEmail = request.POST.get('JAEmail', '')
        anytable = Any(j5text=j5text, J5_Cost=J5_Cost, JAName_First=JAName_First, JAName_Last=JAName_Last,
                       JAMob_num=JAMob_num, JAEmail=JAEmail)
        anytable.save()
        aid = anytable.any_key
        thank = True
        return render(request, 'any.html', {'thank': thank, 'eid': aid})

    return render(request, 'any.html')


def daan(request):
    if request.method == "POST" or request.method == "FILES":
        Donate_Reason = request.POST.get('Donate_Reason', '')
        Donar_mob_num = request.POST.get('Donar_mob_num', '')
        Donation = request.POST.get('Donation', '')
        khayrat = request.POST.get('khayrat', '') == 'on'
        zakat = request.POST.get('zakat', '') == 'on'
        imamezamin = request.POST.get('imamezamin', '') == 'on'
        khums = request.POST.get('khums', '') == 'on'
        anyd = request.POST.get('anyd', '') == 'on'
        obj = DataLogin.objects.all()
        if Donar_mob_num:
            for i in obj:
                print(i.DMob_num)
                if i.DMob_num != Donar_mob_num:
                    check = False
                else:
                    check = True
                    break
        if check:
            daan = Daan(Donate_Reason=Donate_Reason, Donar_mob_num=Donar_mob_num, Donation=Donation, khayrat=khayrat,
                        zakat=zakat, imamezamin=imamezamin, khums=khums, anyd=anyd)
            daan.save()
            did = daan.daan_key
            thank = True
            return render(request, 'daan.html', {'thank': thank, 'eid': did})
        else:
            messages.info(request, 'This number is not registered')
            return render(request, 'daan.html')
    return render(request, 'daan.html')


def datalogin(request):
    if request.method == "POST" or request.method == "FILES":
        D1Name_First = request.POST.get('D1Name_First', '')
        D1Name_Last = request.POST.get('D1Name_Last', '')
        DMob_num = request.POST.get('DMob_num', '')
        DEmail = request.POST.get('DEmail', '')
        obj = DataLogin.objects.all()
        if DMob_num:
            for i in obj:
                print(i.DMob_num)
                if i.DMob_num != DMob_num:
                    checkd = True
                else:
                    checkd = False
                    break
            # print(checkd)
            if checkd:
                datalogin = DataLogin(D1Name_First=D1Name_First, D1Name_Last=D1Name_Last, DMob_num=DMob_num,
                                      DEmail=DEmail)
                datalogin.save()
                return render(request, 'daan.html')
            else:
                messages.info(request, 'This number is already registered')
                return render(request, 'datalogin.html')

    return render(request, 'datalogin.html')



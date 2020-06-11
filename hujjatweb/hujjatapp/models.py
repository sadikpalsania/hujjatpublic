from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

Accepted = 1
Changes = 2
Default = 3
Rejected = 4

status = (
    ('Accepted', 'ACCEPTED'),
    ('Changes', 'CHANGES'),
    ('Default', 'DEFAULT'),
    ('Rejected', 'REJECTED'),
)


class JEducation(models.Model):
    # J1_Edu_Id=models.AutoField()
    # _J1=models.ForeignKey(Jarooriyat,on_delete=models.CASCADE,default='',null=True)
    education_key = models.AutoField(primary_key=True, unique=True)
    JEName_First = models.CharField(max_length=50, default='')
    JEName_Last = models.CharField(max_length=50, default='')
    JEMob_num = models.CharField(max_length=10, blank=True, null=True, default=9876543210)
    J1_Name_First = models.CharField(max_length=50, default='')
    J1_Name_Last = models.CharField(max_length=50, default='')
    J1_Standard = models.CharField(max_length=10, default='')
    J1_Fees = models.CharField(max_length=10, default='')
    J1_Paidfees = models.CharField(max_length=10, default='')
    # J1_Paiddate=forms.DateField(widget=forms.DateInput(format='%d%m%Y'),input_formats=('%d%m%Y'), required=False)
    J1_Paiddate = models.DateField(max_length=10, null=True, blank=True, default=datetime.date.today)
    J1_Rempaidfees = models.CharField(max_length=10, default='')
    J1_Receipt = models.FileField(upload_to="Educational_receipt", null=True, blank=True)
    j1text = models.TextField(max_length=255, default='', blank=True, null=True)
    JEEmail = models.EmailField(max_length=50, default='')
    date_posted = models.DateTimeField(default=timezone.now)
    Status = models.CharField(max_length=10, choices=status, default='Default')

    def __str__(self):
        return self.J1_Name_First


class JMedical(models.Model):
    # J2_Edu_Id=models.AutoField()
    medical_key = models.AutoField(primary_key=True, unique=True)
    JMName_First = models.CharField(max_length=50, default='')
    JMName_Last = models.CharField(max_length=50, default='')
    JMMob_num = models.CharField(max_length=10, blank=True, null=True, default=9876543210)
    J2_Name_First = models.CharField(max_length=50, default='')
    J2_Name_Last = models.CharField(max_length=50, default='')
    j2text = models.TextField(max_length=255, default='')
    J2_HospiName = models.CharField(max_length=20, default='')
    J2_DocName = models.CharField(max_length=20, default='')
    J2_Cost = models.CharField(max_length=10, default='')
    J2_Receipt = models.FileField(upload_to="Medical_receipt", null=True, blank=True)
    JMEmail = models.EmailField(max_length=50, default='')
    date_posted = models.DateTimeField(default=timezone.now)
    Status = models.CharField(max_length=10, choices=status, default='Default')

    def __str__(self):
        return self.J2_Name_First


class JSamajik(models.Model):
    # J3_Samaj_Id=models.AutoField()
    samajik_key = models.AutoField(primary_key=True, unique=True)
    JSName_First = models.CharField(max_length=50, default='')
    JSName_Last = models.CharField(max_length=50, default='')
    JSMob_num = models.CharField(max_length=10, blank=True, null=True, default=9876543210)
    j3text = models.TextField(max_length=255, default='')
    J3_Cost = models.CharField(max_length=15, default='')
    JSEmail = models.EmailField(max_length=50, default='')
    date_posted = models.DateTimeField(default=timezone.now)
    Status = models.CharField(max_length=10, choices=status, default='Default')

    def __str__(self):
        return self.JSName_First


class JPardes(models.Model):
    # J4_Pardes_Id=models.AutoField()
    pardes_key = models.AutoField(primary_key=True, unique=True)
    JPName_First = models.CharField(max_length=50, default='')
    JPName_Last = models.CharField(max_length=50, default='')
    JPMob_num = models.CharField(max_length=10, blank=True, null=True, default=9876543210)
    J4_Name_First = models.CharField(max_length=50, default='')
    J4_Name_Last = models.CharField(max_length=50, default='')
    j4text = models.TextField(max_length=255, default='')
    J4_muddat = models.CharField(max_length=20, default='')
    J4_Cost = models.CharField(max_length=20, default='')
    JPEmail = models.EmailField(max_length=50, default='')
    date_posted = models.DateTimeField(default=timezone.now)
    Status = models.CharField(max_length=10, choices=status, default='Default')

    def __str__(self):
        return self.J4_Name_First


class Any(models.Model):
    # J5_Any_Id=models.AutoField()
    any_key = models.AutoField(primary_key=True)
    JAName_First = models.CharField(max_length=50, default='')
    JAName_Last = models.CharField(max_length=50, default='')
    JAMob_num = models.CharField(max_length=10, blank=True, null=True, default=9876543210)
    j5text = models.TextField(max_length=255, default='')
    J5_Cost = models.CharField(max_length=10, default='')
    JAEmail = models.EmailField(max_length=50, default='')
    date_posted = models.DateTimeField(default=timezone.now)
    Status = models.CharField(max_length=10, choices=status, default='Default')

    def __str__(self):
        return self.JAName_First


class DataLogin(models.Model):
    # D1_Paheli_Id=models.AutoField()
    data_login_key = models.AutoField(primary_key=True,)
    D1Name_First = models.CharField(max_length=20, default='')
    D1Name_Last = models.CharField(max_length=20, default='')
    DMob_num = models.CharField(max_length=10, default='')
    DEmail = models.EmailField(max_length=50, default='')
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.D1Name_First

    # def __unicode__(self):
    #     return self.DMob_num


class Daan(models.Model):
    # Daan_Id=models.AutoField()
    daan_key = models.AutoField(primary_key=True,)
    Donate_Reason = models.CharField(max_length=250, default='')
    Donation = models.CharField(max_length=10, default='')
    Donar_mob_num = models.CharField(max_length=10, default='')
    khayrat = models.BooleanField(default=False)
    zakat = models.BooleanField(default=False)
    imamezamin = models.BooleanField(default=False)
    khums = models.BooleanField(default=False)
    anyd = models.BooleanField(default=False)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Donar_mob_num

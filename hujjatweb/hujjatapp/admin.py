from django.contrib import admin
from django.utils.safestring import mark_safe
# Register your models here.
from .models import JSamajik, DataLogin, JPardes, JMedical, JEducation, Daan, Any

admin.site.site_header = 'Al-Hujjat Admin Panel'
admin.site.site_title = "Al-Hujjat"


def select_default(self, modeladmin, queryset):
    queryset.update(Status='Default')


def select_accept(self, modeladmin, queryset):
    queryset.update(Status='Accepted')


def select_reject(self, modeladmin, queryset):
    queryset.update(Status='Rejected')


def select_change(self, modeladmin, queryset):
    queryset.update(Status='Changes')


select_default.short_description = "Mark selected as Default"
select_accept.short_description = "Mark selected as Accepted"
select_reject.short_description = "Mark selected as Rejected"
select_change.short_description = "Mark selected as Changes"


class HujjatAdminS(admin.ModelAdmin):
    list_display = ('First_Last_Name', 'Status', 'status')
    list_filter = ('Status',)
    list_editable = ('Status',)
    search_fields = ('JSName_First', 'JSName_Last',)
    actions = [select_default, select_accept, select_change, select_reject]
    list_per_page = 10

    def status(self, obj):
        if obj.Status == 'Default':
            return mark_safe('<div style="width:90%%; height:100%%; background-color: #edddd4; padding: 6px;">%s</div>' % obj.Status)
        elif obj.Status == 'Accepted':
            return mark_safe(
                '<div style="width:90%%; height:100%%; background-color: #affc41; padding: 6px;">%s</div>' % obj.Status)
        elif obj.Status == 'Rejected':
            return mark_safe(
                '<div style="width:90%%; height:100%%; background-color: #dc2f02; color:white; padding: 6px;">%s</div>' % obj.Status)
        elif obj.Status == 'Changes':
            return mark_safe(
                '<div style="width:90%%; height:100%%; background-color: #457b9d; color:white; padding: 6px;">%s</div>' % obj.Status)
        return

    def First_Last_Name(self, obj):
        return "{}  {}".format(obj.JSName_First, obj.JSName_Last)


class HujjatAdminP(admin.ModelAdmin):
    list_display = ('First_Last_Name', 'Status', 'status')
    list_filter = ('Status',)
    list_editable = ('Status',)
    search_fields = ('J4_Name_First', 'J4_Name_Last',)
    actions = [select_default, select_accept, select_change, select_reject]
    list_per_page = 10

    def status(self, obj):
        if obj.Status == 'Default':
            return mark_safe(
                '<div style="width:90%%; height:100%%; background-color: #edddd4; padding: 6px;">%s</div>' % obj.Status)
        elif obj.Status == 'Accepted':
            return mark_safe(
                '<div style="width:90%%; height:100%%; background-color: #affc41; padding: 6px;">%s</div>' % obj.Status)
        elif obj.Status == 'Rejected':
            return mark_safe(
                '<div style="width:90%%; height:100%%; background-color: #dc2f02; color:white; padding: 6px;">%s</div>' % obj.Status)
        elif obj.Status == 'Changes':
            return mark_safe(
                '<div style="width:90%%; height:100%%; background-color: #457b9d; color:white; padding: 6px;">%s</div>' % obj.Status)
        return

    def First_Last_Name(self, obj):
        return "{}  {}".format(obj.J4_Name_First, obj.J4_Name_Last)


class HujjatAdminM(admin.ModelAdmin):
    list_display = ('First_Last_Name', 'Status', 'status',)
    list_filter = ('Status',)
    list_editable = ('Status',)
    search_fields = ('J2_Name_First', 'J2_Name_Last',)
    actions = [select_default, select_accept, select_change, select_reject]
    list_per_page = 10

    def status(self, obj):
        if obj.Status == 'Default':
            return mark_safe(
                '<div style="width:90%%; height:100%%; background-color: #edddd4; padding: 6px;">%s</div>' % obj.Status)
        elif obj.Status == 'Accepted':
            return mark_safe(
                '<div style="width:90%%; height:100%%; background-color: #affc41; padding: 6px;">%s</div>' % obj.Status)
        elif obj.Status == 'Rejected':
            return mark_safe(
                '<div style="width:90%%; height:100%%; background-color: #dc2f02; color:white; padding: 6px;">%s</div>' % obj.Status)
        elif obj.Status == 'Changes':
            return mark_safe(
                '<div style="width:90%%; height:100%%; background-color: #457b9d; color:white; padding: 6px;">%s</div>' % obj.Status)
        return

    def First_Last_Name(self, obj):
        return "{}  {}".format(obj.J2_Name_First, obj.J2_Name_Last)


class HujjatAdminE(admin.ModelAdmin):
    list_display = ('First_Last_Name', 'Status', 'status',)
    list_filter = ('Status',)
    list_editable = ('Status',)
    search_fields = ('J1_Name_First', 'J1_Name_Last',)
    actions = [select_default, select_accept, select_change, select_reject]

    list_per_page = 10

    def status(self, obj):
        if obj.Status == 'Default':
            return mark_safe(
                '<div style="width:90%%; height:100%%; background-color: #edddd4; padding: 6px;">%s</div>' % obj.Status)
        elif obj.Status == 'Accepted':
            return mark_safe(
                '<div style="width:90%%; height:100%%; background-color: #affc41; padding: 6px;">%s</div>' % obj.Status)
        elif obj.Status == 'Rejected':
            return mark_safe(
                '<div style="width:90%%; height:100%%; background-color: #dc2f02; color:white; padding: 6px;">%s</div>' % obj.Status)
        elif obj.Status == 'Changes':
            return mark_safe(
                '<div style="width:90%%; height:100%%; background-color: #457b9d; color:white; padding: 6px;">%s</div>' % obj.Status)
        return

    def First_Last_Name(self, obj):
        return "{}  {}".format(obj.J1_Name_First, obj.J1_Name_Last)


class HujjatAdminA(admin.ModelAdmin):
    list_display = ('First_Last_Name', 'Status', 'status',)
    list_filter = ('Status',)
    list_editable = ('Status',)
    search_fields = ('JAName_First', 'JAName_Last',)
    actions = [select_default, select_accept, select_change, select_reject]
    list_per_page = 10

    def status(self, obj):
        if obj.Status == 'Default':
            return mark_safe(
                '<div style="width:90%%; height:100%%; background-color: #edddd4; padding: 6px;">%s</div>' % obj.Status)
        elif obj.Status == 'Accepted':
            return mark_safe(
                '<div style="width:90%%; height:100%%; background-color: #affc41; padding: 6px;">%s</div>' % obj.Status)
        elif obj.Status == 'Rejected':
            return mark_safe(
                '<div style="width:90%%; height:100%%; background-color: #dc2f02; color:white; padding: 6px;">%s</div>' % obj.Status)
        elif obj.Status == 'Changes':
            return mark_safe(
                '<div style="width:90%%; height:100%%; background-color: #457b9d; color:white; padding: 6px;">%s</div>' % obj.Status)
        return

    def First_Last_Name(self, obj):
        return "{}  {}".format(obj.JAName_First, obj.JAName_Last)


admin.site.register(JSamajik, HujjatAdminS)
admin.site.register(JPardes, HujjatAdminP)
admin.site.register(DataLogin)
admin.site.register(JMedical, HujjatAdminM)
admin.site.register(JEducation, HujjatAdminE)
admin.site.register(Daan)
admin.site.register(Any, HujjatAdminA)

from django.contrib import admin

from accounts.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display=['company_name','first_name','is_employee','is_admin']
    fields = ('company_name','first_name','last_name','password','email','phone_number','designation','is_admin','is_company','is_employee','is_staff','is_active','is_superadmin')
    exclude= ("new_pass",)
admin.site.register(Account,AccountAdmin)
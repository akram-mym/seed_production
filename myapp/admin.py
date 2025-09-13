from django.contrib import admin
from myapp.models import Contact,login,employee_info,company


# Register your models here.
admin.site.register(Contact)
admin.site.register(login)
admin.site.register(employee_info)
admin.site.register(company)


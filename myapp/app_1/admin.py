from django.contrib import admin
from .models import AddDetails
# Register your models here.


class AddDetailsAdmin(admin.ModelAdmin):
    fields = ['emailAdd', 'phoneNo', 'gender',
              'bio', 'jobRole', 'interests', 'password']


admin.site.register(AddDetails, AddDetailsAdmin)

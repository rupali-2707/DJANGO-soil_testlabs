from django.contrib import admin

# Register your models here.
from .models import *

from import_export.admin import ImportExportModelAdmin

@admin.register(andhrapradesh,assam,
                bihar,chandigarh,
                Chhattisgarh,delhi,
                goa,gujrat,
                haryana,himachalpradesh,
                jharkhand,karnataka,
                kerala,madhyapradesh,
                maharashtra,meghalaya,
                mizoram,odisha,
                punjab,rajasthan,
                sikkim,tamilnadu,
                telangana,tripura,
                uttarpradesh,uttarakhand)
class ViewAdmin(ImportExportModelAdmin):
    pass

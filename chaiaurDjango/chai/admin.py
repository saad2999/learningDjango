from django.contrib import admin
from .models import chaiVarity,chaiCertificate,Reviews,Store

# 
class ReviewsInline(admin.TabularInline):
    model = Reviews
    extra = 2

class chaiVarityAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'price' , 'dateadded')
    inlines = [ReviewsInline]


class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_Varieties',)

class chaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number', 'issuing_date', 'expiration_date')

admin.site.register(chaiVarity,chaiVarityAdmin)
admin.site.register(Store,StoreAdmin)
admin.site.register(chaiCertificate,chaiCertificateAdmin)


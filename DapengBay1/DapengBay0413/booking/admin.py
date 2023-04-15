from django.contrib import admin

# Register your models here.
from booking.models import member,travel,breakfast,breakfast_shop,dinner_shop,participate,Dinner,Order
admin.site.register(member)
admin.site.register(travel)
admin.site.register(breakfast)
admin.site.register(Dinner)
admin.site.register(breakfast_shop)
admin.site.register(dinner_shop)
admin.site.register(participate)
admin.site.register(Order)
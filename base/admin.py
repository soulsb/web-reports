from django.contrib import admin
from .models import Stock, Stocklog, Sales, Saleslog
# Register your models here.

admin.site.register(Stock)
admin.site.register(Saleslog)
admin.site.register(Stocklog)
admin.site.register(Sales)

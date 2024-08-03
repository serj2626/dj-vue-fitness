from django.contrib import admin
from .models import OrderAbonement, Abonement

@admin.register(Abonement)
class AbonementAdmin(admin.ModelAdmin):
    '''Admin View for Abonement'''

    list_display = ('title', 'price', 'number_of_months', )


@admin.register(OrderAbonement)
class OrderAbonementAdmin(admin.ModelAdmin):
    '''Admin View for OrderAbonement'''

    list_display =  ('user', 'phone', 'abonement', 'start', 'end', 'status', 'active', )
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)
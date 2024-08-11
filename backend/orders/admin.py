from django.contrib import admin

from .models import Abonement, OrderAbonement, OrderTraining


@admin.register(OrderTraining)
class OrderTrainingAdmin(admin.ModelAdmin):
    """Admin View for OrderTraining)"""

    list_display = (
        "user",
        "trainer",
        "start",
        "end",
        "get_rate_title",
        "get_rate_price",
        "get_rate_count_minutes",
        "status",
        "active",
    )

    def get_rate_title(self, obj):
        return obj.rate.title

    def get_rate_price(self, obj):
        return obj.rate.price

    def get_rate_count_minutes(self, obj):
        return obj.rate.count_minutes

    get_rate_title.short_description = "Тариф"
    get_rate_price.short_description = "Цена"
    get_rate_count_minutes.short_description = "Длительность"


@admin.register(Abonement)
class AbonementAdmin(admin.ModelAdmin):
    """Admin View for Abonement"""

    list_display = (
        "id",
        "title",
        "price",
        "description",
        "number_of_months",
    )
    list_editable = (
        "title",
        "price",
        "description",
        "number_of_months",
    )


@admin.register(OrderAbonement)
class OrderAbonementAdmin(admin.ModelAdmin):
    """Admin View for OrderAbonement"""

    list_display = (
        "user",
        "abonement",
        "start",
        "end",
        "get_number_of_months",
        "get_price",
        "status",
        "active",
    )

    def get_number_of_months(self, obj):
        return obj.abonement.number_of_months

    def get_price(self, obj):
        return obj.abonement.price

    get_number_of_months.short_description = "Количество месяцев"
    get_price.short_description = "Цена"

    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)

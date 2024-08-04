from django.contrib import admin
from .models import Rate, RatingStar, RatingTrainer, Trainer, Reviews
from django.utils.html import mark_safe


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    '''Admin View for Reviews'''

    list_display = ('user', 'trainer', 'created_at', )


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    '''Admin View for RatingStar'''

    list_display = ('value',)


@admin.register(RatingTrainer)
class RatingTrainerAdmin(admin.ModelAdmin):
    '''Admin View for RatingTrainer'''

    list_display = ('star', 'trainer', 'user', )


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    '''Admin View for Rate'''

    list_display = ('title', 'count_minutes', 'price',)


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    '''Admin View for Trainer'''

    list_display = ('id', 'position', 'first_name',
                    'last_name', 'email', 'phone', 'get_image')
    list_editable = ('first_name',
                     'last_name', 'email', 'phone',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.avatar.url} style="border-radius: 50%;" " width="100" height="60"')

    get_image.short_description = 'Фото'

    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)

from django.contrib import admin
from django.utils.html import mark_safe

from .models import Post, Rate, RatingStar, Reviews, Subscription, Trainer


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Admin View for Post)"""

    list_display = (
        "title",
        "category",
        "created_at",
        "updated_at",
    )
    save_on_top = True


@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    """Admin View for Reviews"""

    list_display = (
        "user",
        "trainer",
        "get_text",
        "rating",
        "created_at",
    )

    def get_text(self, obj):
        return (obj.text)[:15] + "..."

    get_text.short_description = "Текст отзыва"


@admin.register(RatingStar)
class RatingStarAdmin(admin.ModelAdmin):
    """Admin View for RatingStar"""

    list_display = ("value",)


@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    """Admin View for Rate"""

    list_display = (
        "title",
        "count_minutes",
        "price",
    )


@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    """Admin View for Trainer"""

    list_display = (
        "id",
        "position",
        "first_name",
        "last_name",
        "email",
        "phone",
        "get_image",
    )
    list_editable = (
        "first_name",
        "last_name",
        "email",
        "phone",
    )

    def get_image(self, obj):
        return mark_safe(
            f'<img src={obj.avatar.url} style="border-radius: 50%;" " width="100" height="60"'
        )

    get_image.short_description = "Фото"

    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('',)
    # date_hierarchy = ''
    # ordering = ('',)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    """Admin View for Subscription"""

    list_display = ("email",)

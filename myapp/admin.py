from django.contrib import admin
from .models import Bus, Book, UserProfile, PromoCode, Review, FavouriteRoute, WalletTransaction, Operator


@admin.register(Bus)
class BusAdmin(admin.ModelAdmin):
    list_display = ('bus_name','source','dest','date','time','bus_type','nos','rem','base_price','operator')
    list_filter = ('date','bus_type','source','dest')
    search_fields = ('bus_name','source','dest')
    ordering = ('date','time')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('id','name','email','bus_name','source','dest','date','nos','price','status','refund_status','booked_at')
    list_filter = ('status','refund_status','date')
    search_fields = ('name','email','bus_name')
    ordering = ('-booked_at',)
    readonly_fields = ('booked_at',)


@admin.register(PromoCode)
class PromoCodeAdmin(admin.ModelAdmin):
    list_display = ('code','discount_percent','max_uses','used_count','valid_until','is_active')
    list_editable = ('is_active',)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user','bus','rating','comment','created_at')
    list_filter = ('rating',)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','phone','wallet_balance')


@admin.register(Operator)
class OperatorAdmin(admin.ModelAdmin):
    list_display = ('company_name','user','phone','is_approved')
    list_editable = ('is_approved',)


admin.site.register(FavouriteRoute)
admin.site.register(WalletTransaction)

from django.contrib import admin
from .models import Tweet
# Register your models here.
class TweetAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'message', 'publishing_date')  # Liste görünümünde hangi alanların gösterileceği
    list_filter = ('nickname',)  # Filtreleme yapılacak alanlar


admin.site.register(Tweet,TweetAdmin)
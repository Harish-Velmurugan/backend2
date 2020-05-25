from django.contrib import admin

# Register your models here.
from .models import User_Professional,User_Personal,bids

admin.site.register(User_Personal)
admin.site.register(User_Professional)
admin.site.register(bids)
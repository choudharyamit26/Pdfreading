from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from .models import *

#
# class UserAdmin(BaseUserAdmin):
#     ordering = ['email']
#     list_display = ['email', 'name']
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         (_('Personal Info'), {'fields': ('name',)}),
#         (_('Permissions'),
#          {'fields': ('is_active', 'is_staff', 'is_superuser')}),
#         (_('Important Dates'), {'fields': ('last_login',)})
#     )
#
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'password', 'confirm_password')
#         }),
#     )
#
#
# admin.site.register(User, UserAdmin)

admin.site.register(DailyRenewableGenerationReport)
admin.site.register(DailyRenewableGenerationReportISGS)
admin.site.register(StateControlArea)
admin.site.register(CrawlCount)

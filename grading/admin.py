from django.contrib import admin
from grading.models import MainTask, BonusTask, Student


class StudentAdminInline(admin.TabularInline):
    model = BonusTask


class StudentAdmin(admin.ModelAdmin):
    inlines = (StudentAdminInline,)


admin.site.register(MainTask)
admin.site.register(BonusTask)
admin.site.register(Student, StudentAdmin)

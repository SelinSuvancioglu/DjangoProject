from django.contrib import admin

from MyCv.models import GeneralSetting, Skills, Experience, Education, Documentation


@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameter', 'updated_at', 'created_at']
    search_fields = ['name', 'description', 'parameter']
    list_editable = ['description', 'parameter']

@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ['id', 'order','name', 'percentage', 'updated_at', 'created_at']
    search_fields = ['name']
    list_editable = ['percentage', 'order', 'name']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['id', 'JobTitle', 'JobDetail', 'Company', 'Location', 'StartDate', 'EndDate']
    search_fields = ['JobTitle', 'Company', 'Location']
    list_editable = ['JobTitle', 'JobDetail', 'Company', 'Location' , 'StartDate', 'EndDate']
    class Meta:
        model = Experience

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['id', 'School', 'Degree', 'Department', 'GNO', 'StartDate', 'EndDate']
    search_fields = ['School', 'Degree', 'Department', 'GNO']
    list_editable = ['School', 'Degree', 'Department', 'GNO', 'StartDate', 'EndDate']

@admin.register(Documentation)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ['id', 'order', 'slug', 'button_text', 'file']
    search_fields = ['slug', 'button_text']
    list_editable = ['order', 'slug', 'button_text', 'file']
    class Meta:
        model = Documentation
# Register your models here.

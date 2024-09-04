from django.contrib import admin
from .models import School, Classroom, Teacher, Student


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'address')  # Display these fields in the admin list view


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('grade', 'section', 'school')  # Display these fields in the admin list view
    list_filter = ('grade', 'school')  # Add filters for grade and school


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender')
    list_filter = ('gender',)
    search_fields = ('first_name', 'last_name')  # Enable search by first and last name


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'gender', 'classroom')
    list_filter = ('gender', 'classroom')
    search_fields = ('first_name', 'last_name')

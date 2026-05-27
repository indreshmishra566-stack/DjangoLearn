from django.contrib import admin
from .models import Chapter, Section, Command


class CommandInline(admin.TabularInline):
    model = Command
    extra = 1


class SectionInline(admin.StackedInline):
    model = Section
    extra = 0
    show_change_link = True


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['order', 'icon', 'title', 'slug', 'color']
    list_display_links = ['title']
    prepopulated_fields = {'slug': ('title',)}
    ordering = ['order']
    inlines = [SectionInline]


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['chapter', 'order', 'section_type', 'heading']
    list_filter = ['chapter', 'section_type']
    inlines = [CommandInline]


@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    list_display = ['cmd', 'description', 'section']

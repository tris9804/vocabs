from django.contrib import admin
from .models import Notebook, Vocabulary, Test, Record, Star, User, Sharepermission


admin.site.register(Test)
admin.site.register(Record)
admin.site.register(Sharepermission)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 
    )

@admin.register(Notebook)
class NotebookAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name',
    )

@admin.register(Vocabulary)
class VocabularyAdmin(admin.ModelAdmin):
    list_display = (
        'english', 'chinese',
    )

@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
    list_display = (
        'vocabs',
    )
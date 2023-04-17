from django.contrib import admin
from django.forms import BaseInlineFormSet
from django.core.exceptions import ValidationError
from .models import Article, Scope, Tag


class TagsInlineFormset(BaseInlineFormSet):
    def clean(self):
        counter = 0
        for form in self.forms:
            for x, y in form.cleaned_data.items():
                if x == 'is_main' and y is True:
                    counter += 1
        if counter > 1:
            raise ValidationError('Главный тег может быть всегда только один')
        if counter == 0:
            raise ValidationError('Добавьте главный тег')
        return super().clean()


class TagsInline(admin.TabularInline):
    model = Scope
    formset = TagsInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [TagsInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

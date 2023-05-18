from django import forms
from django.core.exceptions import ValidationError
from django_filters import FilterSet
import django_filters
from .models import Post, Author, PostCategory
import django.forms


# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.

class PostFilter(django_filters.FilterSet):
    """ Набор фильтров для модели Post. """

    title = django_filters.CharFilter(
        field_name='title', label='Заголовок содержит', lookup_expr='icontains',
        widget=django.forms.TextInput(
            attrs={'type': 'text', 'class': "form-control", 'placeholder': "Ведите текст..."}))

    author = django_filters.ModelMultipleChoiceFilter(
        field_name='post_author', label='Выбрать автора', lookup_expr='exact', queryset=Author.objects.all(),
        widget=django.forms.CheckboxSelectMultiple(
            attrs={'type': 'checkbox', 'class': "form-check-inline"}))

    date_time__gt = django_filters.DateFilter(
        field_name="date_created", label="От даты", lookup_expr='gt',
        widget=django.forms.DateInput(
            attrs={'type': 'date', 'class': "form-control"}))

    date_time__lt = django_filters.DateFilter(
        field_name="date_created", label="До даты", lookup_expr='lt',
        widget=django.forms.DateInput(
            attrs={'type': 'date', 'class': "form-control"}))



    class Meta:
        model = Post
        # Порядок в словаре определяет порядок вывода полей в HTML
        fields = ['title', 'author','category' ,'date_time__gt', 'date_time__lt']
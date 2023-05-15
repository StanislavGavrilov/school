from django import template


register = template.Library()


# Регистрируем наш фильтр под именем currency, чтоб Django понимал,
# что это именно фильтр для шаблонов, а не простая функция.
@register.filter()
def censor(value):

   new_word=value.replace ('редиска', 'р******')


   # Возвращаемое функцией значение подставится в шаблон.
   return new_word
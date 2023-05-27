
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
from .filters import PostFilter
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView)
from .forms import PostForm
<<<<<<< HEAD
from django.shortcuts import redirect
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin
=======
>>>>>>> b65e2e99573857ac885070867fa94d2889b4f962


class PostsList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-date_created'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'
    paginate_by = 4


class PostsListSearch(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    # Поле, которое будет использоваться для сортировки объектов
    ordering = '-date_created'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    template_name = 'news_search.html'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    context_object_name = 'news'
    paginate_by = 2

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset, )
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context


# Create your views here.
class PostDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'


<<<<<<< HEAD
class ArticleCreate( PermissionRequiredMixin,CreateView,):
    """ Представление для создания статьи. """
    permission_required = ('news.add_post',)
=======
class ArticleCreate(CreateView):
    """ Представление для создания статьи. """
>>>>>>> b65e2e99573857ac885070867fa94d2889b4f962
    form_class = PostForm
    model = Post
    template_name = 'product_edit.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Добавить статью"
        return context

<<<<<<< HEAD
    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Добавить статью"
        return context

=======
>>>>>>> b65e2e99573857ac885070867fa94d2889b4f962
    def form_valid(self, form):
        post = form.save(commit=False)
        post.category = 'A'
        return super().form_valid(form)


<<<<<<< HEAD
class ArticleUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    """ Представление для редактирования статьи. """

    form_class = PostForm
    model = Post
    template_name = 'product_edit.html'
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
=======
class ArticleUpdate(UpdateView):
    """ Представление для редактирования статьи. """
    form_class = PostForm
    model = Post
    template_name = 'product_edit.html'
>>>>>>> b65e2e99573857ac885070867fa94d2889b4f962

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Редактировать статью"
        return context


class ArticleDelete(DeleteView):
    """ Представление для удаления статьи. """
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts_list')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Удалить статью"
        context['previous_page_url'] = reverse_lazy('posts_list')
        return context


<<<<<<< HEAD
class NewsCreate(PermissionRequiredMixin,CreateView):

    permission_required = ('news.add_post',)
=======
class NewsCreate(CreateView):
>>>>>>> b65e2e99573857ac885070867fa94d2889b4f962
    """ Представление для создания новости. """
    form_class = PostForm
    model = Post
    template_name = 'product_edit.html'

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Добавить новость"
        return context

    def form_valid(self, form):
        post = form.save(commit=False)
        post.category = 'N'
        return super().form_valid(form)


<<<<<<< HEAD
class NewsUpdate(LoginRequiredMixin,PermissionRequiredMixin, UpdateView,):

    permission_required = ('news.change_post',)
=======
class NewsUpdate(UpdateView):
>>>>>>> b65e2e99573857ac885070867fa94d2889b4f962
    """ Представление для редактирования новости. """
    form_class = PostForm
    model = Post
    template_name = 'product_edit.html'
<<<<<<< HEAD
    login_url = '/accounts/login/'
    redirect_field_name = 'redirect_to'
=======
>>>>>>> b65e2e99573857ac885070867fa94d2889b4f962

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Редактировать новость"
        return context


class NewsDelete(DeleteView):
    """ Представление для удаления новости. """
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts_list')

    def get_context_data(self, **kwargs) -> dict:
        context = super().get_context_data(**kwargs)
        context['page_title'] = "Удалить новость"
        context['previous_page_url'] = reverse_lazy('posts_list')
<<<<<<< HEAD
        return context




@login_required
def upgrade_me(request):
    user = request.user
    premium_group = Group.objects.get(name='authors')
    if not request.user.groups.filter(name='authors').exists():
        premium_group.user_set.add(user)
    return redirect('/')
=======
        return context
>>>>>>> b65e2e99573857ac885070867fa94d2889b4f962

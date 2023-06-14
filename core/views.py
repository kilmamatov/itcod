from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, TemplateView, View, DetailView, UpdateView, CreateView
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render, get_object_or_404
from core import models
from .forms import *
from core import filters
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import redirect


# def appleal(request):  # сделать в одну строку
#     count = models.Appeal.objects.count()
#     if count:
#         return HttpResponse(count)
#     else:
#         raise Http404


def appleal_count(request):
    return HttpResponse(get_object_or_404(models.Appeal.objects.count()))


def declarer_phone(request):
    qs = get_object_or_404(models.Declarer.objects.filter(pk=request.GET.get('pk')))
    return HttpResponse(qs.phone)


def no_admin(request):
    return redirect('/admin/')


def val(request):
    return HttpResponse(request.GET)


# def serp(request):
#     object_list = []
#     for p in models.Declarer.objects.filter(phone=request.GET.get('phone')):
#         object_list.append({
#             'id': p.id,
#             'name': p.name,
#             'age': p.age,
#             'gender': p.gender,
#             'phone': p.phone,
#             'health_status': p.health_status
#         })
#         return HttpResponse(object_list)


def serp(request):
    return HttpResponse(models.Declarer.objects.filter(phone=request.GET['phone']).values())


def declarer_js(request, pk):
    object_list = []
    for p in models.Declarer.objects.filter(pk=pk):
        object_list.append({
            'id': p.id,
            'name': p.name,
            'age': p.age,
            'gender': p.gender,
            'phone': p.phone,
            'health_status': p.health_status
        })
    return JsonResponse({'Declarer': object_list})


# def declarer_js(request):
#     p = models.Declarer.objects.filter(pk=request.GET['pk']).values().get()
#     return JsonResponse(p)


# def appeal_detail(request, pk):
#     a = models.Appeal.objects.all()
#     appeals = models.Appeal.objects.filter(pk=pk)
#     service = models.Service.objects.filter(appeals__pk=pk)
#     return render(request, 'core/appeal.html', {'appeals': appeals, 'service': service, 'a': a})


class AppealDetailView(DetailView):
    template_name = 'core/appeal.html'

    def get_queryset(self):
        return models.Appeal.objects.filter(pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['appeals'] = self.get_queryset()
        return context


# def declarer_detail(request, pk):
#     declarers = models.Declarer.objects.filter(pk=pk)
#     return render(request, 'core/declarer.html', {'declarers': declarers})


class DeclarerdDetailView(DetailView):
    template_name = 'core/declarer.html'

    def get_queryset(self):
        return models.Declarer.objects.filter(pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['declarers'] = self.get_queryset()
        return context


# def service_detail(request, pk):
#     services = models.Service.objects.filter(pk=pk)
#     return render(request, 'core/service.html', {'services': services})


class ServiceDetailView(DetailView):
    template_name = 'core/service.html'

    def get_queryset(self):
        return models.Service.objects.filter(pk=self.kwargs.get('pk'))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = self.get_queryset()
        return context


# def appeal_list(request):
#     appeals = models.Appeal.objects.all()
#     return render(request, 'core/appeal_list.html', {'appeals': appeals})


class AppealListView(ListView):
    template_name = 'core/appeal_list.html'
    model = models.Appeal
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.Appeal
    context_object_name = 'appeals'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.filterset_class(data=self.request.GET, queryset=queryset).qs
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset_class(data=self.request.GET).form
        return context


# def index(request):
#     return render(request, 'core/index.html', context={'title': 'Главная страница'})


class Index(TemplateView):
    template_name = 'core/index.html'


# def declarer_list(request):
#     declarers = models.Declarer.objects.all()
#     return render(request, 'core/declarer_list.html', context={'title': 'Список заявителей', 'declarers': declarers})


class DeclarerListView(ListView):
    template_name = 'core/declarer_list.html'
    model = models.Declarer
    filter_backends = [DjangoFilterBackend]
    filterset_class = filters.Declarer
    context_object_name = 'declarers'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = self.filterset_class(data=self.request.GET, queryset=queryset).qs
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset_class(data=self.request.GET).form
        return context


def appeal_create(request):
    title = 'Создание обращения'
    if request.method == 'POST':
        form = ApplealForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ApplealForm()
    return render(request, 'core/appeal_create.html', {'title': title, 'form': form})


# class AppealCreateView(CreateView):
#     template_name = 'core/appeal_create.html'
#     model = models.Appeal
#     form_class = ApplealForm
#     success_url = '/'


def edit_appeal(request):
    title = 'Редактирование обращения'
    appeal = models.Appeal.objects.get(id=request.GET.get('pk'))
    if request.method == 'POST':
        form = ApplealForm(request.POST, instance=appeal)
        if form.is_valid():
            form.save()
    else:
        form = ApplealForm(instance=appeal)
    return render(request, 'core/edit_appeal.html', {'title': title, 'form': form})


# class UpdateAppealView(UpdateView):
#     model = models.Appeal
#     form_class = ApplealForm
#     template_name = 'core/edit_appeal.html'
#     success_url = '/appeal_list'


def declarer_create(request):
    title = 'Создание пользователя'
    if request.method == 'POST':
        form = DeclarerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = DeclarerForm()
    return render(request, 'core/declarer_create.html', {'title': title, 'form': form})


# class DeclarerCreateView(CreateView):
#     template_name = 'core/declarer_create.html'
#     model = models.Declarer
#     form_class = DeclarerForm
#     success_url = '/'


def edit_declarer(request, pk):
    declarer = models.Declarer.objects.get(id=pk)
    if request.method == 'POST':
        form = DeclarerForm(request.POST, instance=declarer)
        if form.is_valid():
            form.save()
    else:
        form = DeclarerForm(instance=declarer)
    return render(request, 'core/edit_declarer.html', {'form': form})


# class UpdateDeclarerView(UpdateView):
#     model = models.Declarer
#     form_class = DeclarerForm
#     template_name = 'core/edit_declarer.html'
#     success_url = '/declarer_list'


def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ServiceForm()
    return render(request, 'core/service_create.html', {'form': form})


# class ServiceCreateView(CreateView):
#     template_name = 'core/service_create.html'
#     model = models.Service
#     form_class = ServiceForm
#     success_url = '/'


def edit_service(request):
    service = models.Service.objects.get(id=request.GET.get('pk'))
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
    else:
        form = ServiceForm(instance=service)
    return render(request, 'core/edit_service.html', {'form': form})


# class UpdateServiceView(UpdateView):
#     model = models.Service
#     form_class = ServiceForm
#     template_name = 'core/edit_service.html'
#     success_url = '/'
#




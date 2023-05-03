from django.db.models import Count, Avg
from django.views.generic import ListView, TemplateView, View
from django.shortcuts import render, get_object_or_404
from core import models
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import redirect


# def appleal(request):
#     count = models.Appeal.objects.count()
#     if count:
#         return HttpResponse(count)
#     else:
#         raise Http404
#
#
# def declarer_phone(request, pk):
#     qs = models.Declarer.objects.get(pk=pk)
#     phone = qs.phone
#     if phone:
#         return HttpResponse(phone)
#     else:
#         raise Http404
#
#
# def no_admin(request):
#     return redirect('/admin/')
#
#
# def val(request, values):
#     return HttpResponse(values)
#
#
# def serp(request, values):
#     object_list = []
#     for p in models.Declarer.objects.filter(phone=values):
#         object_list.append({
#             'id': p.id,
#             'name': p.name,
#             'age': p.age,
#             'gender': p.gender,
#             'phone': p.phone,
#             'health_status': p.health_status
#         })
#         return HttpResponse(object_list)
#
#
# def declarer_js(request, pk):
#     object_list = []
#     for p in models.Declarer.objects.filter(pk=pk):
#         object_list.append({
#             'id': p.id,
#             'name': p.name,
#             'age': p.age,
#             'gender': p.gender,
#             'phone': p.phone,
#             'health_status': p.health_status
#         })
#     return JsonResponse({'Declarer': object_list})


# def appeal_detail(request, pk):
#     a = models.Appeal.objects.all()
#     appeals = models.Appeal.objects.filter(pk=pk)
#     service = models.Service.objects.filter(appeals__pk=pk)
#     return render(request, 'core/appeal.html', {'appeals': appeals, 'service': service, 'a': a})


class appeal_detail(View):
    template_name = 'core/appeal.html'

    def get(self, request, pk):
        a = models.Appeal.objects.all()
        appeals = models.Appeal.objects.filter(pk=pk)
        service = models.Service.objects.filter(appeals__pk=pk)
        return render(request, self.template_name, {'appeals': appeals, 'service': service, 'a': a})


# def declarer_detail(request, pk):
#     declarers = models.Declarer.objects.filter(pk=pk)
#     return render(request, 'core/declarer.html', {'declarers': declarers})


class declarer_detail(View):
    template_name = 'core/declarer.html'

    def get(self, request, pk):
        declarers = models.Declarer.objects.filter(pk=pk)
        return render(request, self.template_name, {'declarers': declarers})


# def service_detail(request, pk):
#     services = models.Service.objects.filter(pk=pk)
#     return render(request, 'core/service.html', {'services': services})


class service_detail(View):
    template_name = 'core/service.html'

    def get(self, request, pk):
        services = models.Service.objects.filter(pk=pk)
        return render(request, self.template_name, {'services': services})


# def appeal_list(request):
#     appeals = models.Appeal.objects.all()
#     return render(request, 'core/appeal_list.html', {'appeals': appeals})


class appeal_list(TemplateView):
    template_name = 'core/appeal_list.html'

    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c['appeals'] = models.Appeal.objects.all()
        return c


# def index(request):
#     return render(request, 'core/index.html', context={'title': 'Главная страница'})


class index(TemplateView):
    template_name = 'core/index.html'


# def declarer_list(request):
#     declarers = models.Declarer.objects.all()
#     return render(request, 'core/declarer_list.html', context={'title': 'Список заявителей', 'declarers': declarers})


class declarer_list(TemplateView):
    template_name = 'core/declarer_list.html'

    def get_context_data(self, **kwargs):
        c = super().get_context_data(**kwargs)
        c['title'] = 'Список заявителей'
        c['declarers'] = models.Declarer.objects.all()
        return c




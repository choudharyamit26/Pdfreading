from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, CreateView, ListView, DetailView, DeleteView, UpdateView

from src.models import UserNotification, DailyRenewableGenerationReport, StateControlArea, \
    DailyRenewableGenerationReportISGS,CrawlCount
from .filters import DailyRenewableGenerationReportFilter, DailyRenewableGenerationReportISGSFilter, \
    StateControlAreaFilter

User = get_user_model()


# Create your views here.
class Dashboard(LoginRequiredMixin, ListView):
    model = DailyRenewableGenerationReport
    template_name = 'dashboard.html'

    def get(self, request, *args, **kwargs):
        latest_crawl = DailyRenewableGenerationReport.objects.last()
        latest_crawl_date = latest_crawl.date
        prev_crawl_count = CrawlCount.objects.all()[0].count
        context = {
            'latest_crawl_date': latest_crawl_date,
            'prev_crawl_count': prev_crawl_count
        }
        return render(self.request, "dashboard.html", context)


class NotificationView(ListView):
    model = UserNotification
    template_name = 'notification.html'


class NotificationCount(ListView):
    def get(self, request, *args, **kwargs):
        count = UserNotification.objects.filter(read=False).count()
        return HttpResponse(count)


class ReadNotifications(ListView):
    def get(self, request, *args, **kwargs):
        notifications = UserNotification.objects.filter(read=False)
        for obj in notifications:
            obj.read = True
            obj.save()
        return HttpResponse('Read all notifications')


class DailyRenewableGenerationReportView(ListView):
    model = DailyRenewableGenerationReport
    template_name = 'DailyRenewableGenerationReport.html'

    def get(self, request, *args, **kwargs):
        report = DailyRenewableGenerationReport.objects.all()
        myfilter = DailyRenewableGenerationReportFilter(self.request.GET, queryset=report)
        report = myfilter.qs
        context = {
            'report': report
        }
        return render(self.request, "DailyRenewableGenerationReport.html", context)


class DailyRenewableGenerationReportISGSView(ListView):
    model = DailyRenewableGenerationReportISGS
    template_name = 'DailyRenewableGenerationReportISGS.html'

    def get(self, request, *args, **kwargs):
        report = DailyRenewableGenerationReportISGS.objects.all()
        myfilter = DailyRenewableGenerationReportISGSFilter(self.request.GET, queryset=report)
        report = myfilter.qs
        context = {
            'report': report
        }
        return render(self.request, "DailyRenewableGenerationReportISGS.html", context)


class StateControlAreaView(ListView):
    model = StateControlArea
    template_name = 'StateControlArea.html'

    def get(self, request, *args, **kwargs):
        report = StateControlArea.objects.all()
        myfilter = StateControlAreaFilter(self.request.GET, queryset=report)
        report = myfilter.qs
        context = {
            'report': report
        }
        return render(self.request, "StateControlArea.html", context)

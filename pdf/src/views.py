import calendar
import csv
import os
import re
import shutil
from datetime import date, timedelta, datetime
from urllib import request

import camelot
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.utils import timezone
from django.views.generic import CreateView, View

from .forms import ImportDataForm
from .models import DailyRenewableGenerationReportISGS, DailyRenewableGenerationReport, StateControlArea, \
    UserNotification, CrawlCount

User = get_user_model()


# path = 'csv'
# if os.path.exists(path):
#     shutil.rmtree("csv")
#     os.makedirs(path)
# else:
#     os.makedirs(path)
# tables = camelot.read_pdf('01.pdf', pages='1-end')
# tables.export('csv/pdf-data.csv', f='csv')
#
# os.chdir("csv")
# print(os.getcwd())
# extension = 'csv'
# all_filenames = [i for i in glob.glob('*.{}'.format(extension))]
# combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
# # export to csv
# combined_csv.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')
# print('after combined csv')
# # if os.path.isdir("csv"):
# #     print('inside if')
# #     os.chdir('csv')
# # for f in os.listdir(''):
# #     print('inside for')
# #     print(f)
# #     # #     os.chdir('./csv')
# #     if f == 'combined_csv':
# with open('combined_csv.csv', encoding="utf8") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
# print(os.getcwd())
# os.chdir('readpdf.py')
# # x = os.getcwd()
# if os.path.isdir("csv"):
#     shutil.rmtree("csv")
#     print('Deleted folder csv successfully')


class ImportPdf(LoginRequiredMixin, CreateView):
    model = DailyRenewableGenerationReport
    form_class = ImportDataForm
    template_name = 'import.html'

    def post(self, *args, **kwargs):
        path = 'media'
        if os.path.exists(path):
            shutil.rmtree("media")
            os.makedirs(path)
        else:
            os.makedirs(path)
        try:
            host = 'http://www.cea.nic.in/reports/daily/renewable/2020/August/'
            # url = "http://www.cea.nic.in/reports/daily/renewable/2020/August/01.pdf"
            c = 1
            for x in range(32):
                d = str(c).zfill(2)
                url = host + d + ".pdf"
                print(url)
                c += 1
                print('<<<<<<<<<<------------------>>>>>>>>>>>>>>>>', c)
                print('<<<<<<<<<<------------------>>>>>>>>>>>>>>>>', type(c))
                folder = "media/" + d + ".pdf"
                request.urlretrieve(url, folder)
                tables = camelot.read_pdf(folder, pages='1-end')
                tables.export('media/pdf-data.csv', f='csv')
                date_1 = ''
                with open('./media/pdf-data-page-1-table-1.csv', encoding="utf8") as file:
                    reader = csv.reader(file)
                    print(reader)
                    i = 0
                    for row in reader:
                        print(row)
                        print(i)
                        i += 1
                        if i == 5:
                            date_1 = row[1]
                        if i > 5:
                            DailyRenewableGenerationReport.objects.create(
                                date=date_1,
                                state_region=row[0],
                                wind_energy=row[1],
                                solar_energy=row[2],
                                hydro_energy=row[3],
                                total=row[4],
                                cum_wind_energy=row[5],
                                cum_solar_energy=row[6],
                                cum_hydro_energy=row[7],
                                cum_total=row[8]
                            )
                with open('./media/pdf-data-page-2-table-1.csv', encoding="utf8") as file:
                    reader = csv.reader(file)
                    print(reader)
                    i = 0
                    for row in reader:
                        print(row)
                        print(i)
                        i += 1
                        if i == 4:
                            date_2 = row[1]
                        if i > 4:
                            DailyRenewableGenerationReportISGS.objects.create(
                                date=date_1,
                                name=row[0],
                                state=row[1],
                                sector=row[2],
                                owner=row[3],
                                type=row[4],
                                installed_capacity=row[5],
                                actual_generation=row[6],
                                cum_generation=row[7],
                                # cum_total=row[8]
                            )
                with open('./media/pdf-data-page-3-table-1.csv', encoding="utf8") as file:
                    reader = csv.reader(file)
                    print(reader)
                    for row in reader:
                        DailyRenewableGenerationReportISGS.objects.create(
                            date=date_1,
                            name=row[0],
                            state=row[1],
                            sector=row[2],
                            owner=row[3],
                            type=row[4],
                            installed_capacity=row[5],
                            actual_generation=row[6],
                            cum_generation=row[7],
                            # cum_total=row[8]
                        )
                with open('./media/pdf-data-page-4-table-1.csv', encoding="utf8") as file:
                    reader = csv.reader(file)
                    print(reader)
                    for row in reader:
                        StateControlArea.objects.create(
                            date=date_1,
                            state_region=row[0],
                            wind_energy=row[1],
                            solar_energy=row[2],
                            hydro_energy=row[3],
                            total=row[4],
                            cum_wind_energy=row[5],
                            cum_solar_energy=row[6],
                            cum_hydro_energy=row[7],
                            cum_total=row[8]
                        )
            prev_crawl_count = CrawlCount.objects.all()[0]
            print('prev_crawl_count----------->>>>>>', prev_crawl_count)
            crawl_count = int(prev_crawl_count)
            crawl_count += 1
            print('curr_crawl_count', crawl_count)
            prev_crawl_count.count = str(crawl_count)
            prev_crawl_count.save(update_fields=['count'])
            if os.path.isdir("media"):
                shutil.rmtree("media")
            print('deleted folder media')
            messages.success(self.request, 'Data uploaded successfully')
            return redirect("admin/")
        except Exception as e:
            print(e)


class ImportSeptemberPdf(View):
    model = DailyRenewableGenerationReport

    def get(self, *args, **kwargs):
        path = 'media'
        if os.path.exists(path):
            shutil.rmtree("media")
            os.makedirs(path)
        else:
            os.makedirs(path)
        try:
            today = str(timezone.now().date())
            print('--->>>', today)
            current_date = today.split('-')
            year = int(current_date[0])
            month = int(current_date[1])
            day = int(current_date[2])
            print(year, month, day)
            current_day = date(year, month, day)
            print('Current day--->>', current_day)
            previous_day = current_day - timedelta(days=1)
            print('Previous Day--->>', previous_day)
            previous_date = str(previous_day).split('-')
            p_year = int(previous_date[0])
            str_year = str(p_year)
            p_month = int(previous_date[1])
            str_month = str(calendar.month_name[p_month])
            print(str_month)
            p_date = int(previous_date[2])
            str_date = str(p_date)
            d = str_date.zfill(2)
            host = "http://www.cea.nic.in/reports/daily/renewable/"
            # url = "http://www.cea.nic.in/reports/daily/renewable/2020/August/01.pdf"
            url = host + str_year + '/' + str_month + '/' + d + '.pdf'
            print(url)
            c = 1
            d = str(c).zfill(2)
            folder = "media/" + d + ".pdf"
            request.urlretrieve(url, folder)
            tables = camelot.read_pdf(folder, pages='1-end')
            tables.export('media/pdf-data.csv', f='csv')
            date_1 = ''
            with open('./media/pdf-data-page-1-table-1.csv', encoding="utf8") as file:
                reader = csv.reader(file)
                # print(reader)
                i = 0
                for row in reader:
                    # print(row)
                    # print(i)
                    i += 1
                    if i == 5:
                        d = row[1].split(' ')
                        m = d[1]
                        month_name = m
                        datetime_object = datetime.strptime(month_name, "%b")
                        month_number = datetime_object.month
                        month_number = str(month_number).zfill(2)
                        date_1 = d[2] + '-' + month_number + '-' + d[0]
                        print(date_1)
                    if i > 5:
                        s = re.sub("[^A-Za-z]", "", row[0].strip())
                        x = list(filter(None, s.split('cid')))
                        for y in x:
                            # print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<', y)
                            DailyRenewableGenerationReport.objects.create(
                                date=date_1,
                                state_region=y,
                                wind_energy=row[1],
                                solar_energy=row[2],
                                hydro_energy=row[3],
                                total=row[4],
                                cum_wind_energy=row[5],
                                cum_solar_energy=row[6],
                                cum_hydro_energy=row[7],
                                cum_total=row[8]
                            )
            with open('./media/pdf-data-page-2-table-1.csv', encoding="utf8") as file:
                reader = csv.reader(file)
                # print(reader)
                i = 0
                for row in reader:
                    # print(row)
                    # print(i)
                    i += 1
                    # if i == 4:
                    #     date_2 = row[1]
                    if i > 4:
                        if row[2] and row[7]:
                            DailyRenewableGenerationReportISGS.objects.create(
                                date=date_1,
                                name=row[0],
                                state=row[1],
                                sector=row[2],
                                owner=row[3],
                                type=row[4],
                                installed_capacity=row[5],
                                actual_generation=row[6],
                                cum_generation=row[7],
                                # cum_total=row[8]
                            )
            with open('./media/pdf-data-page-3-table-1.csv', encoding="utf8") as file:
                reader = csv.reader(file)
                # print(reader)
                for row in reader:
                    if row[2] and row[7]:
                        DailyRenewableGenerationReportISGS.objects.create(
                            date=date_1,
                            name=row[0],
                            state=row[1],
                            sector=row[2],
                            owner=row[3],
                            type=row[4],
                            installed_capacity=row[5],
                            actual_generation=row[6],
                            cum_generation=row[7],
                            # cum_total=row[8]
                        )
            with open('./media/pdf-data-page-4-table-1.csv', encoding="utf8") as file:
                reader = csv.reader(file)
                # print(reader)
                # s = re.sub("[^A-Za-z]", "", row[0].strip())
                # x = list(filter(None, s.split('cid')))
                for row in reader:
                    if row[0] and row[4]:
                        s = re.sub("[^A-Za-z]", "", row[0].strip())
                        x = list(filter(None, s.split('cid')))
                        for y in x:
                            print('>>>>>>>>>>>>>>>>>>>>>>>>> inside pdf-4 ', y)
                            StateControlArea.objects.create(
                                date=date_1,
                                state_region=y,
                                wind_energy=row[1],
                                solar_energy=row[2],
                                hydro_energy=row[3],
                                total=row[4],
                                cum_wind_energy=row[5],
                                cum_solar_energy=row[6],
                                cum_hydro_energy=row[7],
                                cum_total=row[8]
                            )
            if os.path.isdir("media"):
                shutil.rmtree("media")
            print('deleted folder media')
            # messages.success(self.request, 'Data uploaded successfully')
            # return HttpResponseRedirect(self.request.path_info)
            today = timezone.now().date()
            admin = User.objects.get(email='admin@gmail.com')
            UserNotification.objects.create(
                to=admin,
                title='Info',
                body='Data crawled successfully on {}.'.format(today),
                status=True
            )
            prev_crawl_count = CrawlCount.objects.all()[0]
            print('prev_crawl_count----------->>>>>>', prev_crawl_count)
            crawl_count = int(prev_crawl_count.count)
            crawl_count += 1
            print('curr_crawl_count', crawl_count)
            prev_crawl_count.count = str(crawl_count)
            prev_crawl_count.save(update_fields=['count'])
            return HttpResponse('success')
        except Exception as e:
            print('except--->>', e)
            # return HttpResponseRedirect(self.request.path_info)
            today = timezone.now().date()
            admin = User.objects.get(email='admin@gmail.com')
            UserNotification.objects.create(
                to=admin,
                title='Info',
                body='Data was not available  on {}.'.format(today),
                status=False
            )
            return HttpResponse('failure')


class TestApi(View):
    model = DailyRenewableGenerationReport

    def get(self, request, *args, **kwargs):
        x = 'Hello World!'
        return HttpResponse(x)

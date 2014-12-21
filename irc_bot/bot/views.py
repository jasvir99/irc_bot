from irc_bot.bot.models import *
from irc_bot.bot.forms import *
from django.template.response import TemplateResponse
from datetime import datetime, timedelta
def logPage(request):
    if request.method == 'POST':
        form = getDate(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            entered_date = date
            current_date = datetime.now().date()
            if entered_date > current_date:
                error = 'How would I know future? o.O'
                temp = {'form': form,'error': error}
                return TemplateResponse(request, 'bot/getdate.html',temp)
            else:
                midnight = datetime(date.year, date.month, date.day)
                dayafter = datetime(date.year, date.month, date.day) + timedelta(hours=24)
                log = main.objects.filter(time__gte=midnight, time__lt=dayafter)
                if log:
		    temp = {'log': log,'date': date}
                    return TemplateResponse(request,'bot/showlog.html', temp)
                else:
                    error = 'No records found'
                    temp = {'form': form,'error': error}
                    return TemplateResponse(request, 'bot/getdate.html',temp)
        else:
            form = getDate()
            temp = {'form': form,'error': 'invalid value'}
            return TemplateResponse(request, 'bot/getdate.html',temp)
    else:
        form = getDate()
        temp = {'form': form}
        return TemplateResponse(request, 'bot/getdate.html',temp)

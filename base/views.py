from django.shortcuts import render
from django.http import HttpResponse
from .models import Vw_Sales
from django.template import loader
from django.conf import settings
from django.shortcuts import redirect

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

    stock_list = Vw_Sales.objects.all()
    template = loader.get_template('base/index.html')
    context = {
        'stock_list': stock_list,
    }
    return HttpResponse(template.render(context, request))

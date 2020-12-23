from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

from .models import User
from .models import Company

def index(request):
    user_list = User.objects.order_by('name')
    company_list = Company.objects.all()
    result = dict()
    for company in company_list:
        user_list = User.objects.filter(company_id = int(company.id))
        result[company] = list(user_list)
    template = loader.get_template('myapp/index.html')
    context = {
        'result': result,
    }
    return HttpResponse(template.render(context, request))

def processForm(request):
    user_ids = request.POST.getlist('userid')
    company_id = request.POST.getlist('userid')
    companyname = request.POST.getlist('company')
    user_list = request.POST.getlist('username')
    email_list = request.POST.getlist('email')
    for uid, name, email in zip(user_ids, user_list, email_list):
        user_to_update = User.objects.filter(id=int(uid)).first()
        if user_to_update:
            user_to_update.name = name
            user_to_update.email = email
            user_to_update.save()
    
    return HttpResponseRedirect("/app/")
# views ini merupakan render atau menjadikan,mengubah tampilan html/template untuk membantu menghandle proses request dan respones
# seperti get, put, patch, post dll

from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,Webpage,AccessRecord

# Create your views here.

# buat method


def index(request):
  webpages_list = AccessRecord.objects.order_by('date') # untuk query
  date_dict = {'access_records':webpages_list} # untuk object passingan diviews
  return render(request, 'first_app\index.html', context=date_dict) # request karena sifatnya req, index.html itu berada di folder template/first_app, context ini mempasing data dari variable my_dict nanti di tampilkan pada index.html yakni{insert_me}

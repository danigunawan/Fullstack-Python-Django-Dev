# views ini merupakan render atau menjadikan,mengubah tampilan html/template untuk membantu menghandle proses request dan respones
# seperti get, put, patch, post dll

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# buat method


def index(request):
    # return HttpResponse("Hello World")
  my_dict = {'insert_me': "Hello ini dari first_app/index.html!"}
  # return render(request, 'index.html', context=my_dict) # request karena sifatnya req, index.html itu berada di folder template, context ini mempasing data dari variable my_dict nanti di tampilkan pada index.html yakni{insert_me}
  return render(request, 'first_app\index.html', context=my_dict) # request karena sifatnya req, index.html itu berada di folder template/first_app, context ini mempasing data dari variable my_dict nanti di tampilkan pada index.html yakni{insert_me}

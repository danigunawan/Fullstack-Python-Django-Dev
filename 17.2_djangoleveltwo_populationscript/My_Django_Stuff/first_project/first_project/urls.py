# untuk store semua URL pattern project, biasanya dipakai untuk halaman web aplikasi seperti laravel lah routes/web.php nya

"""first_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include #tambahkan ini utk mapping urls django
from first_app import views #maksudnya kita import views.py pada aplikasi folder django web kita first_app 

urlpatterns = [
	url(r'^$',views.index, name='index'), #views merupakan file handler utk requestnya bawaan native python, index disini adalah seperti function/method nya dan index adalah function utk homepagenya
	url(r'^first_app/',include('first_app.urls')), #r'^$first_app fungsi regex utk replace dan include('first_app.urls') adalah utk mapping urls pada aplikasi first_app dan pada urls yang
	#berada di folder aplikasi django firts_app/urls.py nanti akan ada file urls.py mapping berada di aplikasi first_app jadinya ada 2 di core dan di apps 
	#selain itu first_app/ disini adalah base url yang nanti di akses pada http://namadomain/first_app
    url(r'^admin/', admin.site.urls),
]

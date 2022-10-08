from django.contrib import admin

#from firstapp.views import createblok

# Register your models here.
from .models import User;
from .models import define;
from .models import Createblok;


admin.site.register(User);
admin.site.register(define);
admin.site.register(Createblok)

from django.contrib import admin
from .models import *

admin.site.register(MyUser)
admin.site.register(Post)
admin.site.register(Comments)
admin.site.register(Followerslen)
from django.contrib import admin
from .models import Video,Rating,GpuStatus

admin.site.register(Video)
admin.site.register(Rating)
admin.site.register(GpuStatus)

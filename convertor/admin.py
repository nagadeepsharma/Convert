from django.contrib import admin

from .models import (filesUpload)
from .models import (ImageUpload)

admin.site.register(filesUpload)
admin.site.register(ImageUpload)
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RT_Group.settings')
import django
django.setup()
from main.models import Test
from django.forms.models import model_to_dict


k = model_to_dict(Test.objects.all())
print(k)
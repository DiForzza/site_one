import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RT_Group.settings')
import django
django.setup()
from main.models import Test
from django.forms.models import model_to_dict


print(Test.objects.all())
new_dict = {}
for k in Test.objects.all():
    k = model_to_dict(k)
    key = k['id']
    value = k['text']
    new_dict[key] = value

print(new_dict)

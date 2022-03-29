from django.test import TestCase

nums = [55, 44, 33, 22, 11]
if all([i < 56 for i in nums]):
    print('all larger')

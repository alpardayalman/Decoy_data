# myapp/tasks.py
import time
import random

def add_sample_data():
    from .models import SampleData
    while True:
        SampleData.objects.create(value=random.randint(1, 100))
        time.sleep(10)



import os
from uuid import uuid4
from xml.dom import ValidationErr
from django.forms import ValidationError
from django.test import TestCase
from tasks.models import Task

# Create your tests here.

class TaskTestCase(TestCase):
    def setUp(self):
        self.uuid_assigned=uuid4()
        Task.objects.create(id=self.uuid_assigned, task='Do work', status=False)

        
    def test_item_is_added_and_is_not_checked(self):
        task = Task.objects.get(id=self.uuid_assigned)
        self.assertEqual(task.task,"Do work")
        self.assertEqual(task.status,False)

    def test_update_status(self):
        task = Task.objects.get(id=self.uuid_assigned)
        task.status=True
        task.save()
        task = Task.objects.get(id=self.uuid_assigned)
        self.assertEqual(task.status,True)





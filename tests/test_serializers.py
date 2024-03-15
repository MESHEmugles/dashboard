from django.test import TestCase

from rest_framework.test import APIClient
from main.models import Project, Task
from main.serializers import TaskSerializer, ProjectSerializer

class ProjectCRUDTest(TestCase):
  client = APIClient()

  def test_create_project(self):
    data = {
      "name": "New Proj",
      "slug": "new-date",
      "status": "progress"
    }
    response = self.client.post('/projcreate/', data=data, format='json', content_type='application/json')
    self.assertEqual(response.status_code, 201)
    self.assertEqual(Project.objects.count(), 1)
    proj = Project.objects.get()
    self.assertEqual(proj.name, data['name'])
    self.assertEqual(proj.slug, data['slug'])

  def test_retrieve_project(self):
    proj = Project.objects.create(name="New Project", slug='new-project')
    response = self.client.get(f'/projupdate/{proj.id}/')
    self.assertEqual(response.status_code, 200)
    serializer = TaskSerializer(proj)
    self.assertEqual(response.data, serializer.data)

  def test_update_project(self):
    proj = Project.objects.create(name="Old Project", slug= 'old-project')
    data = {
      "name": "Data Updated",
      "slug": "data-updated",
    }
    response = self.client.put(f'/projupdate/{proj.id}/', data=data, format='json', content_type='application/json')
    self.assertEqual(response.status_code, 200)
    proj.refresh_from_db()
    self.assertEqual(proj.name, data['name'])

  def test_delete_project(self):
    proj = Project.objects.create(name="Test proj", slug = 'test-proj')
    response = self.client.delete(f'/projdelete/{proj.pk}/')
    self.assertEqual(response.status_code, 204)
    self.assertEqual(Project.objects.count(), 0)


class TaskCRUDTest(TestCase):
  client = APIClient()

  def create_test_project(self):
    project = Project.objects.create(name="Test Project", slug="test-project", status = "progress")
    return project

  def test_create_task(self):
    project = self.create_test_project()
    data = {
      "name": "Test Task",
      "slug": "test-task",
      "iscompleted": "False",
      "status": "progress",
      "due_date": "2024-03-20T00:00:00Z",
      "priority": 2,
      "proj": project.id,
    }
    response = self.client.post('/taskcreate/', data=data, format='json', content_type='application/json')
    self.assertEqual(response.status_code, 201)
    self.assertEqual(Task.objects.count(), 1)
    task = Task.objects.get()
    self.assertEqual(task.name, data['name'])
    self.assertEqual(task.slug, data['slug'])
    self.assertEqual(task.priority, data['priority'])
    self.assertEqual(task.iscompleted, data['iscompleted'])
    self.assertEqual(task.iscompleted, data['iscompleted'])

  def test_retrieve_task(self):
    project = self.create_test_project()
    task = Task.objects.create(name="Test Task", slug= "test-task", proj=project, iscompleted = False, status = "progress", priority = 2 )
    response = self.client.get(f'taskupdate/{task.pk}/')
    self.assertEqual(response.status_code, 200) 
    serializer = TaskSerializer(task)
    self.assertEqual(response.data, serializer.data)
    self.assertEqual(len(response.data['task']), 1)

  def test_update_task(self):
    project = self.create_test_project()
    task = Task.objects.create(name="Test Task", slug= "test-task", proj=project, iscompleted = False, status = "progress", priority = 2 )
    data = {
      "name": "Updated Task Name",
      "slug": "updated-task-name", 
      "priority": 3,
      "iscompleted": False,
      "due_date": "2024-03-21T00:00:00Z",
      "status": "progress",
    }
    response = self.client.put(f'/taskupdate/{task.id}/', data=data, format='json', content_type='application/json')
    self.assertEqual(response.status_code, 200) 
    task.refresh_from_db()
    self.assertEqual(task.name, data['name'])
    self.assertEqual(task.due_date.strftime("%Y-%m-%d"), data['due_date'])
    self.assertEqual(task.priority, data['priority'])
    self.assertEqual(task.iscompleted, data['iscompleted'])
    self.assertEqual(task.iscompleted, data['iscompleted'])
    self.assertEqual(task.slug, data['slug'])

  def test_delete_task(self):
    project = self.create_test_project()
    task = Task.objects.create(name="Test Task",slug="test-task", proj=project, iscompleted = False, status = "progress", priority = 2 )
    response = self.client.delete(f'/taskdelete/{task.pk}/')
    self.assertEqual(response.status_code, 204)
    self.assertEqual(Task.objects.count(), 0)




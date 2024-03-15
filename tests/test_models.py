from django.test import TestCase
from main.models import Project, Task

class ProjectModelTest(TestCase):
  def test_create_project(self):
    project_name = "Test Project"
    slug = "test-project"
    project = Project.objects.create(name=project_name, slug=slug)
    self.assertEqual(project.name, project_name)
    self.assertEqual(project.slug, slug)

  def test_project_status_choices(self):
    """
    Test that the STATUS_CHOICES are defined as expected.
    """
    expected_choices = [
      ('urgent', 'Urgent'),
      ('progress', 'Progress'),
      ('on_hold', 'On Hold'),
      ('completed', 'Completed')
    ]
    self.assertEqual(Project._meta.get_field('status').choices, expected_choices)

class TaskModelTest(TestCase):
  def test_create_task(self):
    project = Project.objects.create(name="Test Project", slug ="test-project")
    task_name = "Test Task"
    slug = "test-task"
    task = Task.objects.create(name=task_name, slug=slug, proj=project)
    self.assertEqual(task.name, task_name)
    self.assertEqual(task.slug, slug)
    self.assertEqual(task.proj, project)

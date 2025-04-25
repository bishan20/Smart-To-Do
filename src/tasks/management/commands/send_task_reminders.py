from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta
from tasks.models import Task

class Command(BaseCommand):
    help = 'Send email reminders for tasks due tomorrow'

    def handle(self, *args, **kwargs):
        tomorrow = timezone.localdate() + timedelta(days=1)
        tasks_due = Task.objects.filter(due_date=tomorrow, completed=False)

        count = 0
        for task in tasks_due:
            if not task.user.email:
                continue

            subject = f'Reminder: Task "{task.title}" is due tomorrow'
            message = (
                f'Hello {task.user.username},\n\n'
                f'This is a reminder that your task "{task.title}" is due on {task.due_date}.\n\n'
                f'Description: {task.description or "No description"}\n\n'
                f'- Smart To-Do App'
            )
            send_mail(
                subject,
                message,
                'no-reply@smarttodoapp.com',
                [task.user.email],
                fail_silently=False,
            )
            count += 1

        self.stdout.write(self.style.SUCCESS(f'Reminders sent for {count} task(s).'))

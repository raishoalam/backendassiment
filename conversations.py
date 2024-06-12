# cleanup_old_conversations.py

from django.core.management.base import BaseCommand
from yourappname.models import Conversation
from datetime import timedelta
from django.utils import timezone

class Command(BaseCommand):
    help = 'Cleans up old conversations'

    def handle(self, *args, **kwargs):
        # Define a threshold for old conversations (e.g., 30 days)
        threshold_date = timezone.now() - timedelta(days=30)
        
        # Query and delete old conversations
        old_conversations = Conversation.objects.filter(created_at__lt=threshold_date)
        old_conversations.delete()

        self.stdout.write(self.style.SUCCESS('Old conversations cleaned up successfully'))

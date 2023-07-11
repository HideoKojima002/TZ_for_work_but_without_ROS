import logging
from django.core.management.base import BaseCommand

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    def handle(self, *args, **options):
        logger.info("Starting log listener...")
        while True:
            log_data = input("Enter log data: ")
            if log_data:
                if 'error' in log_data:
                    logger.error(log_data)
                else:
                    logger.info(log_data)
            else:
                break
        logger.info("Log listener stopped.")

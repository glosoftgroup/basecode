from django.http import HttpResponse
from app_dir.core import tasks
from structlog import get_logger

logger = get_logger(__name__)


def test_celery(request):
    result = tasks.longtime_add(2, 3)
    logger.info(result)
    return HttpResponse(result)

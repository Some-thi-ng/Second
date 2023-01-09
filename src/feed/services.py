from django.conf import settings
from ..gallery.models import Publication


class Feed:
    # Лента публикаций
    def get_post_list(self, user: settings.AUTH_USER_MODEL):
        return Publication.objects\
            .filter(user__owner__subscriber=user)\
            .order_by('-created_at')\
            .select_related('user')\
            .prefetch_related('comments')

feed_service = Feed()

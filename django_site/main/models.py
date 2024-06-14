from django.db import models
from django.utils.translation import gettext_lazy as _

class Article(models.Model):
    title = models.CharField(_("Title"), max_length=100)
    content = models.TextField(_("Content"))
    publication_date = models.DateTimeField(_("Creation date"), auto_now_add=True)

    class Meta:
        verbose_name = _("Article")
        verbose_name_plural = _("Articles")

    def __str__(self):
        return self.title

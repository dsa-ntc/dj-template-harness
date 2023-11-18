"""Mock Django models for providing templates with a context."""

from django.db import models


class Page(models.Model):
    """A model representing a page.

    Args:
        title: The title of the page.
    """

    title = models.CharField(max_length=255)

    def __str__(self: "Page") -> str:
        return self.title

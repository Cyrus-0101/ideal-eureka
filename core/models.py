from django.db import models
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify
from uuid import uuid4
from tinymce.models import HTMLField

# Create your models here.


class Recipe(models.Model):
    name = models.CharField(
        verbose_name=_("recipe name"),
        max_length=200,
        null=False,
        unique=False,
        blank=False,
        help_text=_("format: required, max-200"),
    )

    description = HTMLField(
        null=False,
        blank=False,
        verbose_name=_("recipe description"),
        help_text=_("format: required"),
    )

    ingredients = HTMLField(
        null=False,
        blank=False,
        verbose_name=_("recipe description"),
        help_text=_("format: required"),
    )

    slug = models.SlugField(
        max_length=150,
        null=True,
        unique=True,
        blank=True,
        verbose_name=_("recipe safe URL"),
        help_text=_(
            "format: required, letters, numbers, underscore, or hyphens"
        ),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("date recipe created"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("date recipe last updated"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    _id = models.UUIDField(primary_key=True, editable=False, default=uuid4)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(
                self.name + '-' + str(uuid4()))
        return super().save(*args, **kwargs)


class Blog(models.Model):
    title = models.CharField(
        verbose_name=_("blog title"),
        max_length=200,
        null=False,
        unique=False,
        blank=False,
        help_text=_("format: required, max-200"),
    )

    description = HTMLField(
        null=False,
        blank=False,
        verbose_name=_("recipe description"),
        help_text=_("format: required"),
    )

    slug = models.SlugField(
        max_length=150,
        null=True,
        unique=True,
        blank=True,
        verbose_name=_("blog safe URL"),
        help_text=_(
            "format: required, letters, numbers, underscore, or hyphens"
        ),
    )

    recipe = models.ForeignKey(
        to=Recipe,
        on_delete=models.DO_NOTHING
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name=_("date blog created"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("date blog last updated"),
        help_text=_("format: Y-m-d H:M:S"),
    )

    is_active = models.BooleanField(
        default=False,
        verbose_name=_("is the blog active?"),
    )

    _id = models.UUIDField(primary_key=True, editable=False, default=uuid4)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(
                self.name + '-' + str(uuid4()))
        return super().save(*args, **kwargs)

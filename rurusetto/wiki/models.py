from django.core.validators import FileExtensionValidator
from django.db import models
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField
from django.contrib.sitemaps import ping_google

RELEASE_TYPE = (
    # In-system value - Show value
    ('pre-release', 'Pre-release'),
    ('stable', 'Stable')
)


class Changelog(models.Model):
    version = models.CharField(default='', max_length=30)
    time = models.DateTimeField(auto_now_add=True)
    type = models.TextField(choices=RELEASE_TYPE, default='stable')
    note = MDTextField()

    def __str__(self):
        return f'{self.version} changelog ({self.type})'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            ping_google()
        except Exception:
            pass


class Ruleset(models.Model):
    creator = models.CharField(default="0", max_length=10)
    owner = models.CharField(default="0", max_length=10)

    name = models.CharField(default="", max_length=20)
    slug = models.SlugField(default="", max_length=20)
    description = models.CharField(default="", max_length=150)
    icon = models.ImageField(default='default_icon.png', upload_to='rulesets_icon', validators=[
        FileExtensionValidator(allowed_extensions=['png', 'gif', 'jpg', 'jpeg', 'bmp', 'svg', 'webp'])])
    logo = models.ImageField(default='default_logo.jpeg', upload_to='rulesets_logo', validators=[
        FileExtensionValidator(allowed_extensions=['png', 'gif', 'jpg', 'jpeg', 'bmp', 'svg', 'webp'])])
    cover_image = models.ImageField(default='default_wiki_cover.jpeg', upload_to='wiki_cover', validators=[
        FileExtensionValidator(allowed_extensions=['png', 'gif', 'jpg', 'jpeg', 'bmp', 'svg', 'webp'])])
    opengraph_image = models.ImageField(default='default_wiki_cover.jpeg', upload_to='rulesets_opengraph_image', validators=[
        FileExtensionValidator(allowed_extensions=['png', 'gif', 'jpg', 'jpeg', 'bmp', 'svg', 'webp'])])
    content = MDTextField()

    source = models.URLField(default="")

    last_edited_by = models.CharField(default="0", max_length=10)
    last_edited_at = models.DateTimeField(auto_now=True, editable=True)
    created_at = models.DateTimeField(auto_now_add=True)
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            ping_google()
        except Exception:
            pass


class Subpage(models.Model):
    ruleset_id = models.CharField(default="0", max_length=10)

    title = models.CharField(default="", max_length=50)
    slug = models.SlugField(default="", max_length=50)

    content = MDTextField()

    creator = models.CharField(default="0", max_length=10)
    last_edited_by = models.CharField(default="0", max_length=10)
    last_edited_at = models.DateTimeField(auto_now=True, editable=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} (Subpage of {Ruleset.objects.get(id=int(self.ruleset_id)).name})'


class CustomWiki(models.Model):
    title = models.CharField(default="", max_length=100)

    time = models.DateTimeField(auto_now_add=True)
    last_edited_at = models.DateTimeField(auto_now=True, editable=True)

    creator = models.CharField(default="0", max_length=10)
    last_edited_by = models.CharField(default="0", max_length=10)

    content = MDTextField()

    def __str__(self):
        return f'{self.version} changelog ({self.type})'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        try:
            ping_google()
        except Exception:
            pass
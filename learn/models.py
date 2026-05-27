from django.db import models


class Chapter(models.Model):
    order = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True)
    icon = models.CharField(max_length=10, default='📄')
    title = models.CharField(max_length=200)
    color = models.CharField(max_length=20, default='#44b78b')

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.order}. {self.title}"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('learn:chapter', kwargs={'slug': self.slug})


class Section(models.Model):
    SECTION_TYPES = [
        ('theory', 'Theory'),
        ('code', 'Code'),
        ('commands', 'Commands'),
    ]
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, related_name='sections')
    order = models.PositiveIntegerField(default=0)
    section_type = models.CharField(max_length=20, choices=SECTION_TYPES)
    heading = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    code = models.TextField(blank=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.chapter.title} — {self.heading}"


class Command(models.Model):
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='commands')
    order = models.PositiveIntegerField(default=0)
    cmd = models.CharField(max_length=300)
    description = models.CharField(max_length=300)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.cmd

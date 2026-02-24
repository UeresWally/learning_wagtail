from django.db import models

from wagtail.models import Page
from wagtail.fields import RichTextField

from wagtail.admin.panels import FieldPanel, MultiFieldPanel


class HomePage(Page):
    image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Homepage Image'
    )
    hero_text = models.CharField(
        max_length=255, 
        blank=True, help_text='Write a introduction for the site'
    )
    hero_cta = models.CharField(
        blank=True,
        verbose_name='Hero CTA',
        max_length=255,
        help_text="Text to display on Call to Action butto",
    )
    hero_cta_link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Select a page to link tofor the call to action'
    )
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel(
            [
                FieldPanel('image'),
                FieldPanel('hero_text'),
                FieldPanel('hero_cta'),
                FieldPanel('hero_cta_link'),
                
            ],
            heading="Hero Section",
        ),
        FieldPanel('body'),
    ]

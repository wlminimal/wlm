from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailadmin.edit_handlers import FieldPanel, FieldRowPanel, InlinePanel, MultiFieldPanel
from wagtail.wagtailsnippets.edit_handlers import SnippetChooserPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from wagtail.wagtailforms.models import AbstractEmailForm, AbstractFormField
from wagtail.wagtailforms.edit_handlers import FormSubmissionsPanel
from modelcluster.fields import ParentalKey


class BasicPage(Page):
    pass


class HomePage(Page):
    slider1_title = models.TextField(max_length=100, help_text='maximum length 100 characters',
                                     default='We\'re a')
    slider1_title_em = models.TextField(max_length=100, help_text='maximum length 100 characters, emphasize character',
                                        default='Digital Studio')
    slider1_subtitle = models.TextField(max_length=200, help_text='maximum legnth 200, subtitle in slider 1',
                                        default='Photography and Web Development at one Best Place')
    slider2_title_em = models.TextField(max_length=100, help_text='maximum length 100 characters and emphasize',
                                        default='Picture')
    slider2_title = models.TextField(max_length=200, help_text='maximum length is 200 characters',
                                     default='is a worth a thousand words')
    slider3_title = models.TextField(max_length=100, help_text='maximum length 100 characters',
                                     default='Based in')
    slider3_title_em = models.TextField(max_length=100, help_text='maximum length 20 characters emphasize',
                                        default='Los Angeles')
    slider3_title_2 = models.TextField(max_length=100, help_text='maximum length 20 characters',
                                        default='Downtown')

    slider1_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Image size must be 1680 x 1100"
    )
    slider2_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Image size must be 1680 x 1100"
    )
    slider3_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Image size must be 1680 x 1100"
    )

    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        websites = WebsitePage.objects.all().live().order_by('-first_published_at')
        context["websites"] = websites
        return context


    # Page body
    page_body_title_1 = models.CharField(max_length=20, help_text='maximum length 20 characters',
                                         default='We\'re a')
    page_body_title_1_em = models.TextField(max_length=30, help_text='maximum length 30 characters, emphasize',
                                         default='digital studio')
    page_body_title_2 = models.TextField(max_length=70, help_text='maximum length 70 characters',
                                         default='that believe in the word of')
    page_body_title_2_em = models.TextField(max_length=30, help_text='maximum length 30 characters, emphasize',
                                         default='less is more')
    page_body_subtitle_1 = models.CharField(max_length=20, help_text='maximum length 20 characters',
                                            default='We')
    page_body_subtitle_em = models.CharField(max_length=20, help_text='maximum length 20 characters, emphasize',
                                            default='really')
    page_body_subtitle_2 = models.CharField(max_length=20,
                                            help_text='maximum length 20 characters',
                                            default='like minimal.')

    service_col_1_header = models.CharField(max_length=100, default="Website Design & Development")
    service_col_1_description = RichTextField(default="Description for service")
    service_col_2_header = models.CharField(max_length=100, default="E-Commerce Web Development")
    service_col_2_description = RichTextField(default="Description for service")
    service_col_3_header = models.CharField(max_length=100, default="Digital Marketing Strategy")
    service_col_3_description = RichTextField(default="Description for service")
    service_col_4_header = models.CharField(max_length=100, default="Creative Photographer")
    service_col_4_description = RichTextField(default="Description for service")

    content_panels = Page.content_panels + [

        FieldPanel('slider1_title', classname='full'),
        FieldPanel('slider1_title_em', classname='full'),
        FieldPanel('slider1_subtitle', classname='full'),
        ImageChooserPanel('slider1_image'),
        FieldPanel('slider2_title_em', classname='full'),
        FieldPanel('slider2_title', classname='full'),
        ImageChooserPanel('slider2_image'),
        FieldPanel('slider3_title', classname='full'),
        FieldPanel('slider3_title_em', classname='full'),
        FieldPanel('slider3_title_2', classname='full'),
        ImageChooserPanel('slider3_image'),

        FieldPanel('page_body_title_1', classname='full'),
        FieldPanel('page_body_title_1_em', classname='full'),
        FieldPanel('page_body_title_2', classname='full'),
        FieldPanel('page_body_title_2_em', classname='full'),

        FieldPanel('page_body_subtitle_1', classname='full'),
        FieldPanel('page_body_subtitle_em', classname='full'),
        FieldPanel('page_body_subtitle_2', classname='full'),

        FieldPanel('service_col_1_header'),
        FieldPanel('service_col_1_description'),

        FieldPanel('service_col_2_header'),
        FieldPanel('service_col_2_description'),

        FieldPanel('service_col_3_header'),
        FieldPanel('service_col_3_description'),

        FieldPanel('service_col_4_header'),
        FieldPanel('service_col_4_description'),
    ]


class PhotographyPage(Page):
    main_title = models.TextField(max_length=40,
                                  help_text='Max Length is 40 characters',
                                  default='Art of Still Image')
    subtitle = models.TextField(max_length=100,
                                help_text='Subtitle, Max Length is 100 characters',
                                default='WLM Studio')
    body = RichTextField(default='This is body of this page.')

    portfolio_image_1 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="1100 x 650 px images."
    )
    portfolio_image_2 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="1100 x 650 px images."
    )
    portfolio_image_3 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="1100 x 650 px images."
    )
    portfolio_image_4 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="1100 x 650 px images."
    )
    portfolio_image_5 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="1100 x 650 px images."
    )
    portfolio_image_6 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="1100 x 650 px images."
    )
    portfolio_image_7 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="1100 x 650 px images."
    )
    portfolio_image_8 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="1100 x 650 px images."
    )


    content_panels = Page.content_panels + [
        FieldPanel('main_title', classname='full'),
        FieldPanel('subtitle', classname='full'),
        FieldPanel('body', classname='full'),
        ImageChooserPanel('portfolio_image_1'),
        ImageChooserPanel('portfolio_image_2'),
        ImageChooserPanel('portfolio_image_3'),
        ImageChooserPanel('portfolio_image_4'),
        ImageChooserPanel('portfolio_image_5'),
        ImageChooserPanel('portfolio_image_6'),
        ImageChooserPanel('portfolio_image_7'),
        ImageChooserPanel('portfolio_image_8'),
    ]

@register_snippet
@python_2_unicode_compatible
class WebsiteCategory(models.Model):
    name = models.CharField(max_length=25,
                            help_text='Name of Website category, max length is 25',
                            default='E-Commerce')

    panels = [
        FieldPanel('name'),
    ]

    def __str__(self):
        return self.name


class WebsitesPage(Page):
    title_1_front = models.CharField(max_length=20,
                               help_text='Max Length is 20 characters',
                               default='We\'re a')
    title_em_middle = models.TextField(max_length=40,
                                help_text='Max Length is 40 characters',
                                default='Web Developer')
    title_1_end = models.TextField(max_length=100,
                                   help_text='Max Length is 100 characters',
                                   default='that make')
    title_2_front = models.TextField(max_length=60,
                                     help_text='Max Length is 60 chracters',
                                     default='the most functional code out of')
    title_2_em_end = models.TextField(max_length=40,
                                      help_text='Max Length is 40 characters',
                                      default='less code')

    subpage_types = ["home.WebsitePage"]

    def get_context(self, request):
        # update context
        context = super(WebsitesPage, self).get_context(request)
        websitesPages = self.get_children().live().order_by('-first_published_at')
        context['websitesPages'] = websitesPages
        return context

    content_panels = Page.content_panels + [
        FieldPanel('title_1_front', classname='full'),
        FieldPanel('title_em_middle', classname='full'),
        FieldPanel('title_1_end', classname='full'),
        FieldPanel('title_2_front', classname='full'),
        FieldPanel('title_2_em_end', classname='full'),
    ]


class WebsitePage(Page):
    project_title = models.CharField(max_length=40,
                                     help_text='Project Name, 40 chracters max',
                                     default='We like minimal')
    project_category = models.CharField(max_length=70,
                                        help_text='Project Category, 70 characters max',
                                        default='E-Commerce')

    website_category = models.ForeignKey(
        'home.WebsiteCategory',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    project_description = RichTextField(default='Describe Proejct Detail')

    website_url = models.URLField(default='www.welikeminimal.com')

    website_image_1 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="1100 x 650 px images."
    )
    website_image_2 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="1100 x 650 px images."
    )
    website_image_3 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="1100 x 650 px images."
    )
    website_image_4 = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="1100 x 650 px images."
    )
    thumbnail_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="600 x anysize(400, 600, 800) px image"
    )

    content_panels = Page.content_panels + [
        FieldPanel('project_title'),
        FieldPanel('project_category'),
        SnippetChooserPanel('website_category'),
        FieldPanel('project_description'),
        FieldPanel('website_url'),
        ImageChooserPanel('thumbnail_image'),
        ImageChooserPanel('website_image_1'),
        ImageChooserPanel('website_image_2'),
        ImageChooserPanel('website_image_3'),
        ImageChooserPanel('website_image_4'),
    ]


class ServicePage(Page):
    main_title1 = models.CharField(max_length=20, default='These are the ', help_text='Main Title, 20 Max Characters')
    main_title1_em = models.CharField(max_length=30, default='things', help_text='Emphasize Text, 30 Max Chracters')
    main_title2 = models.CharField(max_length=20, default='we are ', help_text='Second line title, 20 Max Characters')
    main_title2_em = models.CharField(max_length=30, default='good at.', help_text='Emphasize Text, 30 Max Characters')
    main_subtitle_first = RichTextField(default='Main Subtitle First Line')
    main_subtitle_second = RichTextField(default='Main Subtitle Second Line')

    first_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='300 x 300 px image'
    )
    what_we_do_first = models.CharField(max_length=20, default='Websites', help_text='20 Max Characters')
    first_description = RichTextField(default='Description for what we do')

    second_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='300 x 300 px image'
    )
    what_we_do_second = models.CharField(max_length=20, default='Photography', help_text='20 Max Characters')
    second_description = RichTextField(default='Description for what we do')

    third_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='300 x 300 px image'
    )
    what_we_do_third = models.CharField(max_length=20, default='Build E-Commerce', help_text='20 Max Characters')
    third_description = RichTextField(default='Description for what we do')

    fourth_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='300 x 300 px image'
    )
    what_we_do_fourth = models.CharField(max_length=30, default='E-Commerce Consulting', help_text='30 Max Characters')
    fourth_description = RichTextField(default='Description for what we do')

    fifth_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='300 x 300 px image'
    )
    what_we_do_fifth = models.CharField(max_length=20, default='Ongoing Support', help_text='20 Max Characters')
    fifth_description = RichTextField(default='Description for what we do')

    sixth_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='300 x 300 px image'
    )
    what_we_do_sixth = models.CharField(max_length=20, default='Make Websites', help_text='20 Max Characters')
    sixth_description = RichTextField(default='Description for what we do')

    # Quotes Section
    first_quote = RichTextField(default='When you don\'t create things, you become defined by your tastes rather than ability. your tastes only narrow & exclude people. so create.')
    first_quote_speaker = models.CharField(max_length=30, default='Why The Lucky Stiff', help_text='30 Max Characters')
    second_quote = RichTextField(default='In any moment of decision, the best thing you can do is the right thing, the next best thing is the wrong thing, and the worst thing you can do is nothing.')
    second_quote_speaker = models.CharField(max_length=30, default='Theodore Roosevelt', help_text='30 Max Characters')

    # Price Table Section
    # Website price table
    first_title = models.CharField(max_length=20, default='Website', help_text='Price Table Title, 20 Max Characters')
    first_subtitle = models.TextField(max_length=200, default='First Subtitle', help_text='100 Max Characters')

    first_plan_name = models.CharField(max_length=20, default='Basic', help_text='First plan name for first price table, 20 Max Characters')
    first_plan_description = RichTextField(default='Description for first plan')
    first_plan_price = models.CharField(max_length=40, default='From $1495', help_text='40 Max Characters')

    second_plan_name = models.CharField(max_length=20, default='Premium', help_text='Second plan name for first price table, 20 Max Characters')
    second_plan_description = RichTextField(default='Description for second plan')
    second_plan_price = models.CharField(max_length=40, default='From $3495', help_text='40 Max Characters')

    third_plan_name = models.CharField(max_length=20, default='Ultimate', help_text='Third plan name ofr first price table, 20 Max Characters')
    third_plan_description = RichTextField(default='Description for third plan')
    third_plan_price = models.CharField(max_length=40, default='From $7495', help_text='40 Max Characters')

    # E-Commerce price table
    second_title = models.CharField(max_length=20, default='E-Commerce', help_text='Price Table Title, 20 Max Characters')
    second_subtitle = models.TextField(max_length=200, default='Second Subtitle', help_text='100 Max Characters')

    first_plan_name_2 = models.CharField(max_length=20, default='Basic', help_text='First plan name for second price table, 20 Max Characters')
    first_plan_description_2 = RichTextField(default='Description for first plan in second price table')
    first_plan_price_2 = models.CharField(max_length=40, default='From $2495', help_text='40 Max Characters')

    second_plan_name_2 = models.CharField(max_length=20, default='Premium', help_text='Second plan name for second price table, 20 Max Characters')
    second_plan_description_2 = RichTextField(default='Description for second plan in second price table')
    second_plan_price_2 = models.CharField(max_length=40, default='From 3495', help_text='40 Max Characters')

    third_plan_name_2 = models.CharField(max_length=20, default='Ultimate', help_text='Third plan name for second price table, 20 Max Characters')
    third_plan_description_2 = RichTextField(default='Description for third plan in second price table')
    third_plan_price_2 = models.CharField(max_length=40, default='From $6495', help_text='40 Max Characters')

    # Photography price table
    third_title = models.CharField(max_length=20, default='Photography', help_text='Price Table Title, 20 Max Characters')
    third_subtitle = models.TextField(max_length=200, default='Third Subtitle', help_text='100 Max Characters')

    first_plan_name_3 = models.CharField(max_length=40, default='Event & On Location', help_text='First plan name for third price table, 40 Max Characters')
    first_plan_description_3 = RichTextField(default='Description for first plan in third price table')
    first_plan_price_3 = models.CharField(max_length=40, default='$250 per hour', help_text='40 Max Characters')

    second_plan_name_3 = models.CharField(max_length=40, default='Apparel & Product', help_text='Second plan name for third price table, 40 Max Characters')
    second_plan_description_3 = RichTextField(default='Description for second plan in third price table')
    second_plan_price_3 = models.CharField(max_length=40, default='Charged by piece', help_text='40 Max Characters')

    contact_title_alt = models.TextField(max_length=200, default='We enjoy meeting new people', help_text='100 Max Characters')
    contact_title = models.TextField(max_length=200, default='Interested in working with us?', help_text='100 Max Characters')

    content_panels = Page.content_panels + [
        FieldPanel('main_title1', classname='col6'),
        FieldPanel('main_title1_em', classname='col6'),
        FieldPanel('main_title2', classname='col6'),
        FieldPanel('main_title2_em', classname='col6'),
        FieldPanel('main_subtitle_first'),
        FieldPanel('main_subtitle_second'),
        ImageChooserPanel('first_image'),
        FieldPanel('what_we_do_first'),
        FieldPanel('first_description'),
        ImageChooserPanel('second_image'),
        FieldPanel('what_we_do_second'),
        FieldPanel('second_description'),
        ImageChooserPanel('third_image'),
        FieldPanel('what_we_do_third'),
        FieldPanel('third_description'),
        ImageChooserPanel('fourth_image'),
        FieldPanel('what_we_do_fourth'),
        FieldPanel('fourth_description'),
        ImageChooserPanel('fifth_image'),
        FieldPanel('what_we_do_fifth'),
        FieldPanel('fifth_description'),
        ImageChooserPanel('sixth_image'),
        FieldPanel('what_we_do_sixth'),
        FieldPanel('sixth_description'),
        FieldPanel('first_quote'),
        FieldPanel('first_quote_speaker'),
        FieldPanel('second_quote'),
        FieldPanel('second_quote_speaker'),

        # Price Table
        # Website
        FieldPanel('first_title'),
        FieldPanel('first_subtitle'),

        FieldPanel('first_plan_name'),
        FieldPanel('first_plan_description'),
        FieldPanel('first_plan_price'),

        FieldPanel('second_plan_name'),
        FieldPanel('second_plan_description'),
        FieldPanel('second_plan_price'),

        FieldPanel('third_plan_name'),
        FieldPanel('third_plan_description'),
        FieldPanel('third_plan_price'),


        # E-Commerce
        FieldPanel('second_title'),
        FieldPanel('second_subtitle'),

        FieldPanel('first_plan_name_2'),
        FieldPanel('first_plan_description_2'),
        FieldPanel('first_plan_price_2'),

        FieldPanel('second_plan_name_2'),
        FieldPanel('second_plan_description_2'),
        FieldPanel('second_plan_price_2'),

        FieldPanel('third_plan_name_2'),
        FieldPanel('third_plan_description_2'),
        FieldPanel('third_plan_price_2'),

        # Photography
        FieldPanel('third_title'),
        FieldPanel('third_subtitle'),

        FieldPanel('first_plan_name_3'),
        FieldPanel('first_plan_description_3'),
        FieldPanel('first_plan_price_3'),

        FieldPanel('second_plan_name_3'),
        FieldPanel('second_plan_description_3'),
        FieldPanel('second_plan_price_3'),

        FieldPanel('contact_title_alt'),
        FieldPanel('contact_title'),

    ]


class AboutPage(Page):
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Hero Parallax image, 1680 x 1100'
    )
    est_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text='Established Logo'
    )
    title_small = models.CharField(max_length=70, default='Where the Arts and Technology converge', help_text='First line in the page, 70 Max Characters')
    title_front = models.CharField(max_length=20, default='We are the', help_text='First few letters before emphasize letter')
    title_em = models.CharField(max_length=40, default='Web Agency + Photo Studio', help_text='Emphasize letter, 40 Max Characters')
    title_back = models.TextField(max_length=200, default='based in Los Angeles, crafting digital experiences.')

    main_title = models.TextField(max_length=200, default='Distinctive and striking digital products', help_text='Main title in the page, 200 Max Characters')
    description_left_col = RichTextField(default='Company Description in Left Column')
    description_right_col = RichTextField(default='Company Description in Right Column')

    contact_title_alt = models.TextField(max_length=200, default='We enjoy meeting new people', help_text='100 Max Characters')
    contact_title = models.TextField(max_length=200, default='Interested in working with us?', help_text='100 Max Characters')


    content_panels = Page.content_panels +[
        ImageChooserPanel('hero_image'),
        ImageChooserPanel('est_image'),
        FieldPanel('title_small'),
        FieldPanel('title_front'),
        FieldPanel('title_em'),
        FieldPanel('title_back'),
        FieldPanel('main_title'),
        FieldPanel('description_left_col'),
        FieldPanel('description_right_col'),
        FieldPanel('contact_title_alt'),
        FieldPanel('contact_title'),
    ]


class FormField(AbstractFormField):
    page = ParentalKey('ContactPage', related_name='form_fields')


class ContactPage(AbstractEmailForm):
    hero_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        on_delete=models.SET_NULL,
        help_text='1680 x 1100 image'
    )
    main_title_1 = models.CharField(max_length=40, default='We would love', help_text='Main title, 40 Max Characters')
    main_title_2 = models.CharField(max_length=40, default='to hear from you', help_text='Main title, 40 Max Characters')
    main_subtitle = models.TextField(max_length=100, default='Get in touch with us and we will help you with your next project.', help_text="Main subtitle, 100 Max Length")
    intro_1 = RichTextField(blank=True, default='Start a new project?')
    intro_description = RichTextField(blank=True, default='For quotes on new projects, please fill out our inquiry form and we can direct you to the right team.')
    intro_2 = RichTextField(blank=True, default='Contact us')
    thank_you_text = RichTextField(blank=True, default='Thank you')
    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        ImageChooserPanel('hero_image'),
        FieldPanel('main_title_1', classname='col6'),
        FieldPanel('main_title_2', classname='col6'),
        FieldPanel('main_subtitle'),
        FieldPanel('intro_1'),
        FieldPanel('intro_description'),
        FieldPanel('intro_2', classname='full'),
        InlinePanel('form_fields', label='Form fields'),
        FieldPanel('thank_you_text', classname='full'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname='col6'),
                FieldPanel('to_address', classname='col6'),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

class InquiryFormField(AbstractFormField):
    page = ParentalKey('InquirePage', related_name='inquiry_fields')


class InquirePage(AbstractEmailForm):
    main_title_1 = models.CharField(max_length=40, default='Make an inquiry', help_text='first few letters in main title, 40 Max Characters')
    main_title_2 = models.CharField(max_length=40, default='for', help_text='second line in main title, 40 max characters')
    main_title_em = models.CharField(max_length=40, default='New Project', help_text='Emphasize letter in main title, 40 max characters')
    main_subtitle = models.TextField(max_length=200, default='We will get back to you within 48 hours.', help_text='Main subtitle, 200 max characters')
    intro = RichTextField(default='Please tell us more about your company')
    thank_you_text = RichTextField(blank=False, default='Thank you')

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('main_title_1'),
        FieldPanel('main_title_2', classname='col6'),
        FieldPanel('main_title_em', classname='col6'),
        FieldPanel('main_subtitle'),
        FieldPanel('intro'),
        FieldPanel('thank_you_text', classname='full'),
        InlinePanel('inquiry_fields', label='inquiry fields'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname='col6'),
                FieldPanel('to_address', classname='col6'),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    def get_form_fields(self):
        return self.inquiry_fields.all()

class PhotoInquiryFormField(AbstractFormField):
    page = ParentalKey('PhotoInquirePage', related_name='photo_inquiry_fields')


class PhotoInquirePage(AbstractEmailForm):
    main_title_1 = models.CharField(max_length=40, default='Make an inquiry', help_text='first few letters in main title, 40 Max Characters')
    main_title_2 = models.CharField(max_length=40, default='for', help_text='second line in main title, 40 max characters')
    main_title_em = models.CharField(max_length=40, default='New Photoshoot', help_text='Emphasize letter in main title, 40 max characters')
    main_subtitle = models.TextField(max_length=200, default='We will get back to you within 48 hours.', help_text='Main subtitle, 200 max characters')
    intro = RichTextField(default='Please tell us more about your company')
    thank_you_text = RichTextField(blank=False, default='Thank you')

    content_panels = AbstractEmailForm.content_panels + [
        FormSubmissionsPanel(),
        FieldPanel('main_title_1'),
        FieldPanel('main_title_2', classname='col6'),
        FieldPanel('main_title_em', classname='col6'),
        FieldPanel('main_subtitle'),
        FieldPanel('intro'),
        FieldPanel('thank_you_text', classname='full'),
        InlinePanel('photo_inquiry_fields', label='inquiry fields'),
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('from_address', classname='col6'),
                FieldPanel('to_address', classname='col6'),
            ]),
            FieldPanel('subject'),
        ], "Email"),
    ]

    def get_form_fields(self):
        return self.photo_inquiry_fields.all()

from django import template


register = template.Library()

# @register.assignment_tag(takes_context=True)
# def get_site_root(context):
#     return context['request'].site.root_page

@register.inclusion_tag("home/navbar/navbar.html", takes_context=True)
def display_navbar(context):
    parent = get_site_root(context)
    calling_page = context['self']
    menuitems = parent.get_children().live().in_menu()
    for menuitem in menuitems:
        menuitem.has_children = menuitem.get_children().live().in_menu().exists()
        menuitem.active = (calling_page.url.startswith(menuitem.url) if calling_page else False)

    return {
        "calling_page": calling_page,
        "menuitems": menuitems,
        "request": context['request']
    }


@register.inclusion_tag("home/navbar/dropdown.html", takes_context=True)
def display_dropdown(context, parent):
    submenus = parent.get_children().live().in_menu()

    return {
        "parent": parent,
        "submenus": submenus,
        "request": context['request'],
    }

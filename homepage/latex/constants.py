from django.conf import settings

def site_nmae(context):

    return {'SITE_NAME': settings.SITE_NAME}

__author__ = 'benjamin.c.yan'


def breadcrumb_processor(request):
    return {'breadcrumbs': request.path.split('/')}



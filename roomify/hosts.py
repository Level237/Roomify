from django_hosts import patterns, host

host_patterns = patterns('',
    # sous-domaines dynamiques des hotels → tenant_urls
    host(r'(?P<tenant>[\w-]+)', 'roomify.tenant_urls', name='tenant'),

    # domaine principal (public)
    host(r'www', 'roomify.urls', name='www'),
)
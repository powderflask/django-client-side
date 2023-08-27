"""
Demo client-side CSS / JS dependencies
See: https://github.com/powderflask/django-client-side

External CDN dependencies should match dependency versions in package.json
"""
from django.conf import settings

from client_side.component import Component, DependencySets, Script, Stylesheet

# Each client-side component describes one or more tags to be rendered into HTML

# External core dependencies (mostly loaded from CDN)
#   Protocol is required for PDF generation (seems wkhtmltopdf cannot resolve uri with
#   no protocol designator)
#   See https://www.srihash.org for info on how to generate the hashes
jquery = Component(
    Script(
        url="https://code.jquery.com/jquery-3.3.1.min.js",
        sri="sha384-tsQFqpEReu7ZLhBV2VZlAu7zcOV+rXbYlF2cqB8txI/8aZajjp4Bqd+V6D5IgvKT",
    )
)
bootstrap = Component(
    Script(
        url="https://stackpath.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js",
        sri="sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa",
    ),
    Stylesheet(
        url="https://stackpath.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css",
        sri="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u",
    ),
)

font_antic = Component(
    Stylesheet(
        url="https://fonts.googleapis.com/css?family=Antic",
        # sri causes much weirdness?
        # sri='sha384-zeTATX9tcOoWjsNYmOyWx2/GBjEpUSA7iELDKZ/ak4RswWZBkKsSVzHutF4kEXl4'
    )
)

# bundled JS libraries
lib_common = Component(  # common 3rd party libraries.  Build > npm run build:lib
    Script(url="lib/common.js" if settings.DEBUG else "lib/common.min.js", static=True),
    Stylesheet(url="lib/common.min.css", static=True),
)

# Named, ordered dependency groups.
DEPENDENCIES = DependencySets(
    core=(jquery, bootstrap, lib_common, font_antic),
    shims=(),
    pdf=(bootstrap, font_antic),
)

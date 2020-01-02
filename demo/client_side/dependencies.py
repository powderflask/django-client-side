"""
Demo client-side CSS / JS dependencies

External CDN dependencies should match dependency versions in package.json
"""

# Each client-side resource dependency is a context dictionary with optional fields:
#    script : a dictionary giving the script resource's url, and optionally:  sri (integrity hash), static (boolean)
#    link : a dictionary giving the stylesheet resource's url, and optionally:  sri (integrity hash), static (boolean)
#    ie_condition: the condition for including this dependency as an IE comment condition
#    SETTING: overrides to use when settings.SETTING is Truthy

# External core dependencies
#   Protocol on URL is required for PDF generation (seems wkhtmltopdf cannot resolve uri with no protocol designator)
#   See https://www.srihash.org for info on how to generate the hashes
jquery = {
    'script' : {
        'url' : 'https://code.jquery.com/jquery-3.3.1.min.js',
        'sri' : 'sha384-tsQFqpEReu7ZLhBV2VZlAu7zcOV+rXbYlF2cqB8txI/8aZajjp4Bqd+V6D5IgvKT'
    }
}
bootstrap = {
    'script' : {
        'url' : 'https://stackpath.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js',
        'sri' : 'sha384-Tc5IQib027qvyjSMfHjOMaLkfuWVxZxUPnCJA7l2mCWNIpG9mGCD8wGNIcPD7Txa'
    },
    'link'    : {
        'url' : 'https://stackpath.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css',
        'sri' : 'sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u'
    }
}

font_antic = {
    'link' : {
        'url' : 'https://fonts.googleapis.com/css?family=Antic',
        # 'sri' : 'sha384-zeTATX9tcOoWjsNYmOyWx2/GBjEpUSA7iELDKZ/ak4RswWZBkKsSVzHutF4kEXl4'  # Causes much weirdness?
    }
}

# bundled JS libraries
lib_common = {  # common 3rd party libraries.  Build > npm run build:lib
    'script' : {
        'url'    : 'lib/common.min.js',
        'static' : True
    },
    'link'    : {
        'url'    : 'lib/common.min.css',
        'static' : True
    },
    'DEBUG' : {
        'script': {
            'url'   : 'lib/common.js',
            'static': True
        },
    }
}

# HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries
html5shiv = {
    'ie_condition' : 'lt IE 9',
    'script'       : {
        'url' : 'https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js',
    }
}
respond = {
    'ie_condition' : 'lt IE 9',
    'script'       : {
        'url' : 'https://oss.maxcdn.com/respond/1.4.2/respond.min.js',
    }
}
ie8shim = {
    'ie_condition' : 'lt IE 9',
    'link'          : {
        'url'    : 'css/ie8shim.css',
        'static' : True,
    }
}
ie10viewport = {  # IE10 viewport hack for Surface / desktop Windows 8 bug
    'script' : {
        'url'    : 'bootstrap/js/ie10-viewport-bug-workaround.js',
        'static' : True,
    }
}

# Named, ordered dependency sets.
# This dictionary is the value of settings.CLIENT_SIDE_DEPENDENCIES
DEPENDENCIES = {
    'core' : (jquery, bootstrap, lib_common, font_antic),

    'shims' : (html5shiv, respond, ie8shim, ie10viewport),

    'pdf' : (bootstrap, font_antic),
}
"""
Test dependencies for client-side tests
"""

component = {
    'script': {
        'url': 'https://example.com/component.js',
        'sri': 'sha384-js-sri-here'
    },
    'link': {
        'url': 'https://example.com/component.css',
        'sri': 'sha384-css-sri-here'
    }
}

# conditional components
hijack = {
    'ENABLE_HIJACK': {
        'script': {
            'url': 'https://example.com/hijack.js',
        },
        'link': {
            'url': 'https://example.com/hijack.css',
        }

    }
}

# local static resources
lib_common = {
    'script': {
        'url': 'lib/common.min.js',
        'static': True
    },
    'link': {
        'url': 'lib/common.min.css',
        'static': True
    },
    'DEBUG': {
        'script': {
            'url': 'lib/common.js',
            'static': True
        },
        'link': {
            'url': 'lib/common.css',
            'static': True
        },
    }
}

# IE8 conditional shim
html5shiv = {
    'ie_condition': 'lt IE 9',
    'script': {
        'url': 'https://somecdn.com/html5shiv.min.js',
    }
}

# Named, ordered dependency sets.
# This dictionary is the value of settings.CLIENT_SIDE_DEPENDENCIES
DEPENDENCIES = {
    'core': (component, hijack, lib_common),

    'shims': (html5shiv, ),
}

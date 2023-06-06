# Django Client-side dependency demo app

Demonstrates how to use django-client-side to manage a set of client-side dependencies.

 * Version: 0.1.0
 * Author: powderflask
 * Author URI: https://github.com/powderflask/django-client-side
 * License: MIT  see LICENSE

OVERVIEW:
--------
This app does nothing except present a homepage with some basic external and internal client-side dependencies.
Demo uses npm as both JS package manager and build-tool - but feel free to use any tools you prefer.

Install & Build Demo:
--------------------

* `pip install -r requirements.txt`
* `python3 setup.py test`   (to run app test suite)

* Example: use NPM as client-side pacakge manager and build tool:
     1) Install node and npm globally: https://docs.npmjs.com/getting-started/installing-node
        > brew install node
     2) > npm install
     3) > npm run build
     4) OR  `> npm run watch`  `> npm run watch:kill;`  // when working on JS development

* run django dev server and view in browser to render page with all client-side dependencies loaded.

Notes:
------
 * Local custom source client-side code is in `src` folder - npm build process bundles these into app dependencies.
 * Build scripts install app dependency files into demo `static` folder - files in this folder can be cleaned out: "> npm run clean"
 * Use of `static` folder with django app allows dependency files to be collected with other static files by `> manage.py collectstatic`
 * If settings.DEBUG==True, then un-minified versions are injected, otherwise minified versions for production.
 
Gotchas:
-------
    Partitioning out CDN modules:
    ----------------------------
    Keeping large 3rd party js modules out of bundles is a challenge with node / browserify.
    The modules (jquery, bootstrap, etc.) are better delivered from CDN, but node wants to bundle them in the package.
    Using browserify-shim "expose globals" technique:  https://github.com/thlorenz/browserify-shim#a-expose-global-variables-via-global
    But the shim MUST be applied to all dependencies using the --global flag.  See: https://github.com/thlorenz/browserify-shim/issues/152#issuecomment-412722903
    
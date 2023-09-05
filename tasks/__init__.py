from invoke import Collection
from . import clean, deps, pypi


namespace = Collection(clean, deps, pypi)

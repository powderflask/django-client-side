from invoke import task
from . import clean as clean_task


@task
def clean(c):
    """Clean up dist [and docs] directory"""
    c.run("rm -fr ./dist/*")


@task(pre=[clean], post=[clean_task.clean_all])
def build(c):
    """Clean up and build a new distribution [and docs]"""
    c.run("python -m build")


@task
def get_version(c):
    """Return current version using bumpver"""
    c.run("bumpver show --no-fetch")


@task(help={
    "api-token": "Obtain an API key from https://pypi.org/manage/account/",
    "repo": "Specify:  pypi  for a production release.",
})
def upload(c, api_token, repo="testpypi"):
    """Upload build to given PyPI repo"""
    c.run(f"twine upload --repository {repo} -u __token__ -p {api_token} dist/*")


@task(help={"dist": "Name of distribution file under dist/ directory to check."})
def check(c, dist):
    """Twine check the given distribution"""
    c.run(f"twine check dist/{dist}")


@task(pre=[clean], post=[clean_task.clean_all],
      help={
    "repo": "Specify:  pypi  for a production release.",
          "api-token": "Override config.pypi.api_token, obtained from from https://pypi.org/manage/account/",
      })
def release(c, repo="testpypi", api_token=None):
    """Build release and upload to PyPI"""
    api_token = api_token or c.config.pypi[repo].api_token
    print("Fetching version...")
    get_version(c)
    if input("Continue? (y/n): ").lower()[0] != "y":
        print("Release aborted.")
        exit(0)
    print("Building new release...")
    build(c)
    print(f"Uploading release to {repo}...")
    upload(c, api_token, repo)
    print("Success! Your package has been released.")

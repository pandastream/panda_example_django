from setuptools import setup, find_packages

install_requires = ['panda>=0.1.1']
try:
    import json
except ImportError:
    install_requires.append('simplejson>=2.1.0')

setup(
    name = "panda_example_django",
    version = "0.1.2",
    packages = find_packages(),
    author = "New Bamboo",
    author_email = "info@new-bamboo.co.uk",
    description = "An example of how to integrate Panda on your Django application",
    url = "http://github.com/newbamboo/panda_example_django",
    install_requires=install_requires,
    include_package_data=True,
)
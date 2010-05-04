from setuptools import setup, find_packages

install_requires = ['panda>=0.1.2']
try:
    import json
except ImportError:
    install_requires.append('simplejson>=2.1.0')

setup(
    name = "panda_example_django",
    version = "1.1",
    packages = find_packages(),
    author = "New Bamboo",
    author_email = "info@new-bamboo.co.uk",
    description = "An example of how to integrate Panda on your Django application",
    url = "http://github.com/newbamboo/panda_example_django",
    install_requires=install_requires,
    include_package_data=True,
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
    ],
    license='MIT',
    keywords='panda video encoding stream service example',
)
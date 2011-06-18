import sys
from setuptools import setup, find_packages

peavy = __import__('peavy')
setup(
    author = 'Fairview Computing LLC',
    author_email = 'john@fairviewcomputing.com',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: System :: Logging',
    ],
    description = peavy.__doc__,
    download_url='http://github.com/fairview/django-peavy/downloads',
    install_requires = [
        'Django>=1.3',
        'South>=0.7.2'
    ],
    license = "MIT License",
    name = 'django-peavy',
    packages = find_packages(),
    package_data = {
        'peavy': [
            'README.rst',
            'LICENSE.txt',
            'templates/*/*.html',
           'static/*/*/*',
        ],
    },
    url = 'http://github.com/fairview/django-peavy',
    version = peavy.get_version(),
    zip_safe = True,
)
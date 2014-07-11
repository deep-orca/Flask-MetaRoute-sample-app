"""
Flask-MetaRoute sample application
-------------

Demo app for Flask-MetaRoute package
"""
from setuptools import setup

setup(
    name = 'fmr_sample_app',
    version = '0.0.1',
    description = '',
    license='BSD',
    author='Orca',
    author_email='deep.orca@gmail.com',
    url = 'https://github.com/deep-orca/Flask-MetaRoute-sample-app',
    install_requires = [
        "Flask",
        "paste",
        "Flask-MetaRoute"
    ],
    packages = ['fmr_sample_app'],
    include_package_data = True,
    test_suite = 'nose.collector',
    zip_safe = False,
    entry_points = """
    [paste.app_factory]
    main = fmr_sample_app:make_app
    """
)
"""
Flask-MetaRoute sample application
-------------

Flask-MetaRoute adds some useful decorators for routing
"""
from setuptools import setup

setup(
    name = 'fmr_sample_app',
    version = '0.0.1',
    description = '',
    license='BSD',
    author='Orca',
    author_email='deep.orca@gmail.com',
    url = '',
    install_requires = [
        "Flask",
        "pastedeploy",
        "paste",
        "Flask_MetaRoute"
    ],
    packages = ['fmr_sample_app'],
    include_package_data = True,
    test_suite = 'nose.collector',
    zip_safe = False,
    entry_points = """
    [paste.app_factory]
    main = fmr_sample_app.app:make_app
    """
)
from setuptools import setup, find_packages

version = '4.0.5.dev0'

setup(name='plone.app.contentrules',
      version=version,
      description="Plone integration for plone.contentrules",
      long_description=open("README.rst").read() + "\n\n" + open("CHANGES.rst").read(),
      classifiers=[
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Plone :: 5.0",
          "Framework :: Zope2",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
      ],
      keywords='',
      author='Plone Foundation',
      author_email='plone-developers@lists.sourceforge.net',
      url='http://pypi.python.org/pypi/plone.app.contentrules',
      license='GPL version 2',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plone', 'plone.app'],
      include_package_data=True,
      zip_safe=False,
      extras_require={'test': 'plone.app.testing'},
      install_requires=[
          'setuptools',
          'plone.contentrules',
          'plone.memoize',
          'plone.stringinterp',
          'plone.uuid',
          'plone.autoform',
          'plone.app.z3cform',
          'plone.app.vocabularies',
          'transaction',
          'zope.annotation',
          'zope.browser',
          'zope.component',
          'zope.container',
          'zope.event',
          'zope.i18nmessageid',
          'zope.interface',
          'zope.lifecycleevent',
          'zope.publisher >= 3.11.0',
          'zope.schema',
          'zope.site',
          'zope.traversing',
          'Acquisition',
          'Products.CMFPlone',
          'Products.CMFCore',
          'Products.GenericSetup',
          'Products.statusmessages',
          'ZODB3',
          'Zope2 >= 2.12.3',
      ],
      )

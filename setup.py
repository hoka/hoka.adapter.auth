from setuptools import setup, find_packages

version = '2.13.19.3'

setup(name='hoka.adapter.auth',
      version=version,
      description='Adapter to get the authenticated user',
      long_description=open("README.rst").read(),
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: Web Environment",
          "Framework :: Plone",
          "Framework :: Zope2",
          "Intended Audience :: Other Audience",
          "Intended Audience :: System Administrators",
          "License :: OSI Approved :: GNU General Public License (GPL)",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Internet :: WWW/HTTP :: Site Management :: Link Checking",
        ],
      keywords='adapter user authenticated zope2 hoka',
      author='Kai Hoppert',
      author_email='kai.hoppert@online.de',
      url='https://github.com/hoka/hoka.adapter.auth',
      license='GPL version 2',
      packages=find_packages(),
      namespace_packages=['hoka','hoka.adapter'],
      include_package_data=True,
      install_requires=[
        'setuptools',
        'Zope2',
        'z3c.autoinclude',
        'hoka.patches.get_adapter',
        'hoka.adapter.base',

      ],
      extras_require={'test': [
        'collective.testcaselayer',
      ]},
      platforms='Any',
      zip_safe=False,
      entry_points='''
[z3c.autoinclude.plugin]
target = zope
''',
)
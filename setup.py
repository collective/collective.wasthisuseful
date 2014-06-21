from setuptools import setup, find_packages
import os

version = '1.1'

setup(name='collective.wasthisuseful',
      version=version,
      description="Simple yes/no usefulness rating for Plone content, enables e-mail notification",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Office/Business :: Groupware",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone rating useful e-mail',
      author='Kees Hink',
      author_email='hink@gw20e.com',
      url='https://github.com/collective/collective.wasthisuseful',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'plone.browserlayer',
          'plone.app.registry',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )

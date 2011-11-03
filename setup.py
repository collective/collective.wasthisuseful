from setuptools import setup, find_packages
import os

version = '0.1dvl'

setup(name='collective.wasthisuseful',
      version=version,
      description="Simple yes/no usefulness rating for Plone content, enables e-mail notification",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone rating useful e-mail',
      author='Kees Hink',
      author_email='hink@gw20e.com',
      url='http://svn.plone.org/svn/collective/collective.wasthisuseful',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )

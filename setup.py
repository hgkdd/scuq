import os
from distutils.core import setup
import version

ver=''
version.remember_version(ver)

setup(name='scuq',
      version=version.get_version(),
      author="Thomas Reidemeister, Hans Georg Krauthaeuser",
      author_email="hgk@ieee.org",
      description='scalar and complex uncertain pysical quantities',
      license='All rights reserved',
      url='http://tu-dresden.de/et/tet',
	  packages=['scuq'],
      data_files=[('scuq', ['scuq/LICENSE'])],
      )
#!/usr/bin/env python
#
# Copyright 2016 Feei. All Rights Reserved
#
# Author:   Feei <wufeifei@wufeifei.com>
# Homepage: https://github.com/wufeifei/cobra
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
#
# See the file 'doc/COPYING' for copying permission
#
from distutils.core import setup

setup(name='Cobra',
      version='1.0',
      description='Code Security Scan System',
      author='Feei',
      author_email='wufeifei@wufeifei.com',
      url='https://github.com/wufeifei/cobra',
      packages=['distutils', 'distutils.command'],
      )

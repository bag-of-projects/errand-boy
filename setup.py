#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import errand_boy

package_name = 'errand_boy'
test_package_name = '%s_test_project' % package_name

setup(name='errand-boy',
	version=errand_boy.__version__,
	description="Establish a client/server connection to the errand-boy deamon to execute commands without the memory overhead incurred by os.fork().",
	author='Seán Hayes',
	author_email='sean@seanhayes.name',
	classifiers=[
		"Development Status :: 3 - Alpha",
		"Intended Audience :: Developers",
		"Intended Audience :: System Administrators",
		"License :: OSI Approved :: BSD License",
		"Programming Language :: Python",
		"Topic :: Software Development :: Libraries",
		"Topic :: Software Development :: Libraries :: Python Modules"
	],
	keywords='os fork process memory celery',
	url='https://github.com/SeanHayes/errand-boy',
	download_url='https://github.com/SeanHayes/errand-boy',
	license='BSD',
	packages=[
		package_name,
	],
	include_package_data=True,
	test_suite = '%s.runtests.runtests' % test_package_name,
)

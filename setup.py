from setuptools import setup
import re, os

on_rtd = os.getenv('READTHEDOCS') == 'True'

requirements = []
with open('requirements.txt') as f:
  requirements = f.read().splitlines()

if on_rtd:
  requirements.append('sphinxcontrib-napoleon')

version = ''
with open('discord_unofficial/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set')

readme = ''
with open('README.md') as f:
    readme = f.read()

extras_require = {
    'voice': ['PyNaCl==1.0.1'],
}

setup(name='discord.py-unofficial',
      author='RandomGamer123',
      url='https://github.com/RandomGamer123/discord.py-unofficial',
      version=version,
      packages=['discord_unofficial', 'discord_unofficial.ext.commands'],
      license='MIT',
      description='A python wrapper for the Discord API',
      long_description=readme,
      long_description_content_type="text/markdown",
      include_package_data=True,
      install_requires=requirements,
      extras_require=extras_require,
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
      ]
)

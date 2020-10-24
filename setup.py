from setuptools import setup, find_packages
from os import path
import os.path

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

# Get the long description from the README file
with open("README.md", encoding="utf-8") as f:
    read_file = f.read()
 
setup(
  name='notifly',
  version='1.1.4',
  description='Telegram Bot Notifier',
  long_description=read_file,
  long_description_content_type='text/markdown',
  url='https://github.com/rexdivakar/Telegram-Notifly',  
  author='Divakar R',
  author_email='rexdivakar@hotmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Telegram', 
  packages=['telegram'],
  install_requires=['requests'] 
)

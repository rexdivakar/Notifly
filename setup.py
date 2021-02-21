from setuptools import setup
from os import path

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
  version='1.3.1',
  description='Notification on the fly !',
  long_description=read_file,
  long_description_content_type='text/markdown',
  url='https://github.com/rexdivakar/Telegram-Notifly',  
  author='Divakar R, Sanchit Jain' ,
  author_email='rexdivakar@hotmail.com , sanchitjain1996@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Bot Notification', 
  packages=['notifly'],
  install_requires=['requests', 'numpy==1.19.3', 'matplotlib', 'slackclient', 'python-dotenv', 'psutil']
)

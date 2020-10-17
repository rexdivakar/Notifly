from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='Telegram-Notify',
  version='0.0.2',
  description='Telegram Bot Notifier',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='',  
  author='Divakar R',
  author_email='rexdivakar@hotmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords='Telegram,Telegram-Bot,Telegram-notification', 
  packages=find_packages(),
  install_requires=[''] 
)
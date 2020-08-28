from setuptools import setup, find_packages

setup(name='quasimode', 
      version='0.1',
      packages=find_packages(),
      url='https://github.com/yizaochen/quasimode_pnas16mer.git',
      author='Yizao Chen',
      author_email='yizaochen@gmail.com',
      install_requires=[
          'matplotlib',
      ]
      )
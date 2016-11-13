from setuptools import setup, find_packages

setup(name='eyebrow',
      version='0.0.1',
      description='Raise an eyebrow!',
      long_description="This module has a Eyebrow exception which you can raise when you are confused",
      url='https://github.com/itslukej/eyebrow',
      author='Luke J.',
      author_email='me+eyebrow@lukej.me',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False
)

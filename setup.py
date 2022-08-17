from setuptools import setup, find_packages

with open('README.md', 'r') as file:
    long_description = file.read()

requirements = ["beautifulsoup4>=4.11.1", "coloredlogs>=15.0.1", "selenium"
                                                                 ">=4.4.0",
                "lxml>=4.9.1"]

setup(name='avitoparser',
      version='0.1',
      url='https://github.com/Lonely-Dark/avitoparser',
      license='GPLv3',
      author='Lonely Dark',
      description='Parse the avito website',
      long_description=long_description,
      long_description_content_type="text/markdown",
      zip_safe=False,
      packages=find_packages(),
      install_requires=requirements,
      classifiers=[
          "Programming Language :: Python :: 3",
          "Programming Language :: Python",
          "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
      ],
      )

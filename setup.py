from setuptools import setup, find_packages


def readme():
    with open('README.rst') as f:
        return f.read()

setup(
    name='my_energenie',
    version='0.1',
    description="Home automation scripts using Energenie",
    long_description=(readme()),
    long_description_content_type='text/markdown',
    url="https://github.com/tastatham/jgi-seed-core",
    author="Thomas Statham",
    author_email="tastatham@gmail.com",
    keywords="home automation Energenie",
    license="MIT",
    include_package_data=False
    )


from setuptools import setup, find_packages

setup(
    name='jexelapi',
    version='1.0.8',
    packages=find_packages(),
    description='This library helps to optimize the creation of APIs with FastAPI',
    long_description=open('readme.md',encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    author='Jexel Gómez',
    author_email='jexelg53@gmail.com',
    url='https://github.com/jexelbytes/jexelapi',
    install_requires=[
        'jinja2',
        'shutils'
    ]
)
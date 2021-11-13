from setuptools import find_packages, setup

setup(
    name='musiquepy-website',
    version='1.0.0',
    description='Musiquepy site web principal',
    author='Vitor Moura',
    author_email='mail@mail.com',
    url='https://github.com/vitormoura',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask'        
    ],
)

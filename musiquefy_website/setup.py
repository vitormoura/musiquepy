from setuptools import find_packages, setup

setup(
    name='musiquefy-website',
    version='1.0.0',
    description='Musiquefy site web principal',
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

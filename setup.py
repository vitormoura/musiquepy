from setuptools import find_packages, setup

with open("README.md", 'r') as f:
    long_description = f.read()

with open("requirements.txt", "r") as f:
    requirements = f.readlines()

setup(
    name='musiquepy',
    author='Vitor Moura',
    author_email='mail@mail.com',
    packages=find_packages(),
    scripts=[
        './bin/musiquepy_api_run',
        './bin/musiquepy_website_run'
    ],
    url='http://github.com/vitormoura/musiquepy',
    license='LICENSE',
    description="l'application webapi du projet musiquepy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    setup_requires=['wheel'],
    zip_safe=False,
    install_requires=requirements,
    python_requires='>=3.8'
)

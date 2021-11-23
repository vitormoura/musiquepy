from setuptools import find_packages, setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='musiquepy',
    author='Vitor Moura',
    author_email='mail@mail.com',
    packages=find_packages(),
    scripts=[
        'bin/run_musiquepy.api.py',
        'bin/run_musiquepy.website.py'
    ],
    url='http://github.com/vitormoura/musiquepy',
    license='LICENSE',
    description="l'application webapi du projet musiquepy",
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    setup_requires=['wheel'],
    zip_safe=False,
    install_requires=[
        "pytest==6.2.5",
        "Flask==2.0.2",
        "Flask-Assets==2.0",
        "Flask-Session==0.4.0",
        "autopep8==1.6.0",
        "cssmin==0.2.0",
        "email-validator==1.1.3",
        "pyScss==1.3.7",
        "python-dotenv==0.19.2",
        "WTForms==3.0.0"
    ],
    python_requires='>=3.8'
)

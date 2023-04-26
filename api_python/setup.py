from setuptools import setup, find_packages

setup(
    name='cdstheque',
    version='0.1',
    url="http://127.0.0.1:5000",
    packages=find_packages(),
    description='bibliotheque de cds',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.9',
    ],
    install_requires=[
        'flask',
        'flask-restx',
        'sqlalchemy',
    ],
)

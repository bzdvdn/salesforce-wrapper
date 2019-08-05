from setuptools import setup, find_packages

setup(
    name='salesforce-wrapper',
    version='0.0.1',
    packages=find_packages(),
    install_requires = [
        'requests>=2.18.2'
    ],
    description='SalesForce wrapper',
    author='bzdvdn',
    author_email='bzdv.dn@gmail.com',
    url='https://github.com/bzdvdn/salesforce-wrapper.git',
    license='MIT',
    python_requires=">=3.6",
)
from setuptools import setup

setup(
    # Needed to silence warnings (and to be a worthwhile package)
    name='likelycause',
    url='https://github.com/Ana-c-ng/likelycause',
    author='Ana Garcia',
    author_email='ana.n.garcia2@gmail.com',
    # Needed to actually package something
    packages=['likelycause'],
    # Needed for dependencies
    install_requires=['scipy','sklearn', 'statsmodels'],
    # *strongly* suggested for sharing
    version='0.1',
    # The license can be anything you like
    license='MIT',
    description='A quick way to get the likely cause',
    # We will also need a readme eventually (there will be a warning)
    # long_description=open('README.txt').read(),
)

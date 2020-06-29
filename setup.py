import setuptools

#with open('README.md') as f:
#    README = f.read()

setuptools.setup(
    author="Ana Garcia",
    author_email="ana.n.garcia2@gmail.com",
    name='likelycause',
    license="MIT",
    description='Likely caue has a clever way to identify suspicious',
    version='v0.0.1',
    long_description='README.md',
    url='https://github.com/Ana-c-ng/likelycause',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=['scipy','sklearn','statsmodels'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7.10'
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)

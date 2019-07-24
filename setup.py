import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RunDeck",
    version="0.0.1",
    author="Rory Murdock",
    author_email="rory@itmatic.com.au",
    description="A Library for interacting with RunDeck",
    # long_description=long_description,
    # long_description_content_type="text/markdown",
    url="https://github.com/rorymurdock/RunDeck-Py",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'reqREST',
    ],
)
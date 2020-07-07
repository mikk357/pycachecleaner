import setuptools

try:
    with open("README.md", "r") as fh:
        long_description = fh.read()
except:
    long_description = "smol thing to kill."


setuptools.setup(
    name="pycachecleaner",
    version="0.1.0",
    author="mikk357",
    author_email="mikk357@yandex.com",
    description="smol thing to kill.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mikk357/pycachecleaner",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
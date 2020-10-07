import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="whichtok", 
    version="0.0.1",
    author="Sarah Chen",
    author_email="sarahlc888@gmail.com",
    description="Library for TikTok graph analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sarahlc888/whichtok",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="langchain_search1api",
    version="0.1.0",
    author="Arash Behmand",
    author_email="arashbehmand@gmail.com",
    description="LangChain tools for the search1api service",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/arashbehmand/langchain_search1api",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "langchain>=0.2.0",
        "requests>=2.25.0",
        "pydantic>=2.5.0",
    ],
)

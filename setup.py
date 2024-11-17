from setuptools import setup

setup(
    name="title",  # Name of the library
    version="1.0.0",  # Version of the library
    py_modules=["title"],  # This will include the title.py module
    description="A simple Python library to change the terminal window title",  # Short description
    author="SupremeXD",  # Your name (can be your real name or handle)
    author_email="neon321ontg@gmail.com",  # Your email
    url="https://github.com/SupremeXD4925/TitleLibrary",  # URL to the library (GitHub repo, for example)
    long_description=open('README.md').read(),  # A long description, usually from README.md
    long_description_content_type="text/markdown",  # Content type for the README
    license="MIT",  # License for your code
    classifiers=[  # Classifiers help people find your package
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify the minimum Python version needed
)

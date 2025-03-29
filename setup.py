from setuptools import setup, find_packages

setup(
    name="advanced_python_utilities",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",
        "click",
        "rich"
    ],
    entry_points={
        "console_scripts": [
            "pyutils=cli:cli"
        ]
    },
    description="Advanced Python utilities package with CLI",
    author="willy Hundun",
    author_email="spc.cody.hunter@gmail.com",
    url="https://github.com/yourusername/advanced-python-utilities",
)

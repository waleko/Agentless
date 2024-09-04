from setuptools import setup, find_packages

setup(
    name='agentless',
    version='1.0.0',
    url='https://github.com/mypackage.git',
    author='Author Name',
    author_email='author@gmail.com',
    description='Description of my package',
    packages=find_packages(),
    install_requires=[
        "openai",
        "pre-commit",
        "datasets",
        "tiktoken",
        "swebench",
        "libcst"
    ]
)

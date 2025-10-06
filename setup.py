from setuptools import setup, find_packages

# Load dependencies from the dependencies section of pyproject.toml
# Note: You need to manually copy your dependencies here for a true setup.py approach.
# If you don't want to maintain the list in two places, you can skip this step, but
# using find_packages() and setup() explicitly is still beneficial for clarity.

setup(
    name='semantiker',
    version='0.1.0',
    description='A highly flexible and agnostic semantic caching layer for LLM applications.',
    author='Sandeep Nigam',
    author_email='sandeepnigam379@gmail.com',
    packages=find_packages(),
    install_requires=[
        "numpy",
        "requests",
        "sentence-transformers",
        "faiss-cpu",
        # Note: Added these back since they were in your previous TOML list
    ],
    # metadata for upload to PyPI
    license='MIT',
    keywords=['llm', 'cache', 'semantic-caching', 'rag', 'faiss'],
    url='https://github.com/sandynigs/semantiker',
)
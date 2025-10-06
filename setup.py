from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='semantiker',
    # 🚨 IMPORTANT: Increment the version number
    version='0.1.1',
    description='A highly flexible and agnostic semantic caching layer for LLM applications.',
    
    # --- ADD THESE LINES ---
    long_description=long_description,
    long_description_content_type='text/markdown',
    # -----------------------
    
    author='Sandeep Nigam',
    author_email='sandeepnigam379@gmail.com',
    packages=find_packages(),
    install_requires=[
        "numpy",
        "requests",
        "sentence-transformers",
        "faiss-cpu",
    ],
    license='MIT',
    keywords=['llm', 'cache', 'semantic-caching', 'rag', 'faiss'],
    url='https://github.com/sandynigs/semantiker',
)
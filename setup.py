from setuptools import setup
import pathlib
here = pathlib.Path('README.md').parent.resolve()

setup(
    name = 'MinHeap',
    packages = ['MinHeap'],
    description='A min-Heap that utilizes numpy memmaps so memory consumption can be reduced.',
    long_description=(here / 'README.md').read_text(encoding='utf-8'),
    long_description_content_type='text/markdown',
    version = '2.0',
    license='MIT',
    author = 'Harold J. Iwen',
    author_email = 'inventorsniche349@gmail.com',
    url = 'https://www.inventorsniche.com',
    download_url = 'https://github.com/Hiwen-STEM/MinHeap',
    keywords = ['Binary_Tree', 'Heap','Tree','Min_Heap','Binary'],
    install_requires=[
        'numpy',
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',     
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ]
)

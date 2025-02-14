from setuptools import setup, find_packages

setup(
    name='ft8_generator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'scipy',
        'matplotlib',
    ],
    author='Rintazero',
    author_email='CIRCODE@126.com',
    description='A package for generating FT8 waveforms from payloads.',
    url='https://github.com/yourusername/ft8_generator',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)

from setuptools import setup

setup(
    name='mistrik',
    packages=['mistrik'],
    version='1.0.1',    
    description='Measure text comprehensibility/readability using the Mistrik formula',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/MatusValko/Mistrik',
    author='Matúš Valko',
    author_email='mvmatusvalko@gmail.com',    
    license='MIT',
    
    install_requires=[],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License', 
        'Natural Language :: Slovak',
        'Natural Language :: English',
        'Operating System :: OS Independent',   
        'Topic :: Scientific/Engineering',     
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.12',
    ],
)  
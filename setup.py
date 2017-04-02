# coding: utf-8
import codecs
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

def read_description(filename):
    with codecs.open(filename, encoding='utf-8') as f:
        try:
            import pypandoc
            return pypandoc.convert_text(f.read(), format='md', to='rst')
        except ImportError:
            return f.read()

setup(
    name='input-paste',
    version='0.1.2',
    author='Stephen Chen',
    author_email='g1222888@gmail.com',
    url='https://github.com/RPing/input-paste',
    description='Linux上利用剪貼簿協助打中文的工具',
    long_description=read_description('README.md'),
    keywords='chinese input helper paste clipboard imfix',
    license='MIT',
    packages=['input_paste'],
    entry_points={'console_scripts': [
        'input-paste = input_paste:main',
    ]},
    include_package_data=True,
    classifiers = [
        'Operating System :: Unix',
        'Environment :: X11 Applications',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
)

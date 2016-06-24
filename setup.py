from setuptools import setup
from setuptools.command.install import install as install_

class install(install_):
    def run(self):
        install_.run(self)

setup(
    cmdclass = { 'install' : install },
    name = 'miru16-example',
    version = '0.1',
    author = 'tatsy',
    author_email = 'tatsy.mail@gmail.com',
    url = 'https://github.com/tatsy/miru16-example.git',
    description = 'Example math package for Wakate-no-kai at MIRU 2016',
    license = 'MIT',
    classifiers = [
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'
    ],
    packages = [
        'miru16'
    ]
)

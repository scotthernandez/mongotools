from setuptools import setup, Extension

setup(name='mongomem',
    version='0.1',
    author='Adam Flynn',
    author_email='adam@contextlogic.com',
    description="A tool to analyze MongoDB memory usage by collection",
    keywords="mongodb",
    license="MIT",
    url="http://www.github.com/ContextLogic/mongodbtools",

    ext_modules=[
          Extension('ftools', ['python-ftools/ftools.c']),
    ],
    entry_points={
        'console_scripts': [
            'mongomem = mongomem:main'
        ]
    },
    scripts=['mongomem.py']
)

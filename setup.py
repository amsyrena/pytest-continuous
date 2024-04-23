from setuptools import setup

setup(
    name='pytest-continuous',
    version='0.1.3'
            '',
    description='A pytest plugin to run tests continuously until failure or interruption.',
    packages=['pytest_continuous'],
    entry_points={
        'pytest11': [
            'continuous = pytest_continuous.plugin',
        ],
    },
    classifiers=[
        "Framework :: Pytest",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)

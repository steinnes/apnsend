from setuptools import setup
from pip.req import parse_requirements
from pip.download import PipSession

setup(
    name='apnsend',
    version='0.1',
    description='apnsend is a tool to test your APNS certificate, key and token.',
    py_modules=['apnsend'],
    install_requires=[
        str(req.req) for req in parse_requirements("requirements.txt", session=PipSession())
    ],
    entry_points='''
        [console_scripts]
        apnsend=apnsend:main
    ''',
)

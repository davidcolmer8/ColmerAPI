from setuptools import setup

setup(
    name='stocksSharesApi',
    version='0.1',
    py_modules=['stocksSharesApi'],
    install_requires=[
        'Flask',
        'Click',
        'flasgger',
        'flask_restful'
    ],
    entry_points={
        'console_scripts':[
            'colmerapi = stocksSharesApi.cli:cli'
        ]
    },
)
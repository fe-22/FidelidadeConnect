from setuptools import setup, find_packages

setup(
    name='FidelidadeConnect',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Flask==2.0.2',
        'pandas==1.4.3',
        'waitress==2.1.0',
    ],
    entry_points={
        'console_scripts': [
            'run_fidelidade_connect = run_waitress:main',
        ],
    },
)

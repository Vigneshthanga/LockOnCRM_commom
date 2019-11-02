from setuptools import setup

setup(
    name='LockOnCRM-Common',
    description='Common LockOnCRM classes and functions',
    version='0.4',
    packages=['lockoncrm_common'],
    install_requires=[
        'cachetools',
        'docker',
        'flask-httpauth',
        'python-etcd',
        'pyjwt'
    ]
)

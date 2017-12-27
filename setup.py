from distutils.core import setup

setup(
    name="crak_revenue_affiliate_api",
    version="0.1.0",
    author="Chaps",
    author_email="drumchaps@gmail.com",
    maintainer="Chaps",
    maintainer_email="drumchaps@gmail.com",
    url="https://bitbucket.org/drumchaps/crak_revenue_affiliate_api",
    packages=[
        "crak_revenue_affiliate_api",
    ],
    package_dir={'': 'src'},
    install_requires=["requests", "pytest"]
)

from setuptools import setup

setup(
    name = "GoPhish",
    version = "0.0.2",
    author = "graylagx2",
    author_email = "graylagx2@gmail.com",
    description = ("Social engineering tool for credential harvesting"),
    url = "https://github.com/graylagx2/GoPhish",
    packages=['gophish'],
    package_dir={'gophish': 'src'},
    package_data={'gophish': ['res/*']},
    install_requires=[
        'colorama',
        'pyfiglet==0.8.post1',
        'pyshorteners',
        'selenium',
        'watchdog'
    ],
    entry_points = {
        'console_scripts': ['gophish = src.gophish.__main__:main']
    }
)

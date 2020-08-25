import setuptools

with open("README.md", "r") as file:
    long_description = file.read()

setuptools.setup(
    name='Miraculix',
    version='0.0.1',
    author='Lukas Lamm',
    author_email='lukas.lamm@ifam.rwth-aachen.de',
    url='https://www.ifam.rwth-aachen.de',
    packages=setuptools.find_packages(),
    scripts=[],
    description='A handy tool for examination processes at RWTH Aachen University',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
       "randomuser",
       "docxtpl",
    ],
    python_requires='>=3.5',
    license='LICENSE.md',
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "License :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)
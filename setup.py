from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="omega_conf_resolver",
    version="0.01",
    packages=["omega_conf_resolver"],
    url="",
    license="",
    author="Timo Osterburg",
    author_email="timo.osterburg@tu-dortmund.de",
    description="Collection of costum omegaconf resolver",
    long_description=long_description,
    long_description_content_type="text/markdown",
    project_urls={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "hydra-core",
    ],
    package_dir={"": "src"},
    python_requires=">=3.7",
)

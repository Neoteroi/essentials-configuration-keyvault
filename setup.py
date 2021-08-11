from setuptools import setup


def readme():
    with open("README.md") as f:
        return f.read()


setup(
    name="essentials-configuration-keyvault",
    version="0.0.2",
    description=("Azure Key Vault source for essentials-configuration"),
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/Neoteroi/essentials-configuration-keyvault",
    author="RobertoPrevato",
    author_email="roberto.prevato@gmail.com",
    keywords="Azure Key Vault secrets configuration environment",
    license="MIT",
    packages=["configuration.keyvault"],
    install_requires=[
        "azure-identity==1.6.0",
        "azure-keyvault-secrets==4.3.0",
        "essentials-configuration>=0.0.2",
    ],
    include_package_data=True,
    zip_safe=False,
)

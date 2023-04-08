![Build](https://github.com/Neoteroi/essentials-configuration-keyvault/workflows/Build/badge.svg)
[![pypi](https://img.shields.io/pypi/v/essentials-configuration-keyvault.svg)](https://pypi.python.org/pypi/essentials-configuration-keyvault)
[![versions](https://img.shields.io/pypi/pyversions/essentials-configuration-keyvault.svg)](https://github.com/Neoteroi/essentials-configuration-keyvault)
[![codecov](https://codecov.io/gh/Neoteroi/essentials-configuration-keyvault/branch/main/graph/badge.svg)](https://codecov.io/gh/Neoteroi/essentials-configuration-keyvault)
[![license](https://img.shields.io/github/license/Neoteroi/essentials-configuration-keyvault.svg)](https://github.com/Neoteroi/essentials-configuration-keyvault/blob/main/LICENSE)

# essentials-configuration-keyvault
[Azure Key
Vault](https://docs.microsoft.com/en-us/azure/key-vault/general/overview)
source for
[`essentials-configuration`](https://github.com/Neoteroi/essentials-configuration).

```bash
pip install essentials-configuration-keyvault
```

`essentials-configuration` provides a way to handle configuration roots
composed of different layers, such as configuration files and environmental
variables. Layers are applied in order and can override each others' values,
enabling different scenarios like configuration by environment (e.g. DEV, TEST,
PROD) and system instance.

`essentials-configuration-keyvault` provides a solution to add secrets stored
in Azure Key Vault into configuration objects.

Example:

```python
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from config.common import ConfigurationBuilder
from config.keyvault import KeyVaultSource

key_vault_name = "example-keyvault-name"

secrets_client = SecretClient(
    vault_url=f"https://{key_vault_name}.vault.azure.net",
    credential=DefaultAzureCredential(),
)

builder = ConfigurationBuilder(KeyVaultSource(secrets_client))

# when the configuration object is built, secrets are fetched from
# the linked key vault and put into the configuration object (e.g.
# database connection strings, API keys for SendGrid, etc.)
config = builder.build()
```

> Refer to the [official Key Vault documentation for more
> information about its Python client library.](https://docs.microsoft.com/en-us/azure/key-vault/secrets/quick-create-python).

## How to run the tests using a real Key Vault

The provided tests can either use a mocked `SecretClient`, or use a real Key Vault.
To use a real Key Vault service:

1. create a Key Vault ([ref.](https://docs.microsoft.com/en-us/azure/key-vault/secrets/quick-create-python))
2. sign-in using any way supported by `azure.identity.DefaultAzureCredential` 3
   (e.g. VS Code or `az login`)
3. run the tests with the following command:

```bash
KEYVAULT_NAME="<YOUR_KEYVAULT_NAME>" pytest -s
```

![Build](https://github.com/Neoteroi/essentials-configuration-keyvault/workflows/Build/badge.svg)
[![pypi](https://img.shields.io/pypi/v/essentials-configuration-keyvault.svg)](https://pypi.python.org/pypi/essentials-configuration-keyvault)
[![versions](https://img.shields.io/pypi/pyversions/essentials-configuration.svg)](https://github.com/Neoteroi/essentials-configuration-keyvault)
[![codecov](https://codecov.io/gh/Neoteroi/essentials-configuration-keyvault/branch/main/graph/badge.svg)](https://codecov.io/gh/Neoteroi/essentials-configuration-keyvault)
[![license](https://img.shields.io/github/license/Neoteroi/essentials-configuration-keyvault.svg)](https://github.com/Neoteroi/essentials-configuration/blob/main/LICENSE)

# essentials-configuration-keyvault
[Azure Key
Vault](https://docs.microsoft.com/en-us/azure/key-vault/general/overview)
source for
[`essentials-configuration`](https://github.com/Neoteroi/essentials).

```bash
pip install essentials-configuration-keyvault
```

`essentials-configuration` provides a way to handle configuration roots
composed of different layers, such as configuration files and environmental
variables. Layers are applied in order and can override each others' values,
enabling different scenarios like configuration by environment and system
instance.

`essentials-configuration-keyvault` provides a solution to add secrets stored
in Azure Key Vault into configuration objects.

Example:

```python
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient
from configuration.common import ConfigurationBuilder
from configuration.keyvault import KeyVaultSource

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

## How to run the tests against a real Key Vault
The provided tests can either use a mocked `SecretClient`, or run
against a real Key Vault. To run against a real service:

1. create a key vault
2. sign-in using any way supported by `azure.identity.DefaultAzureCredential` (e.g. VS Code or `az login`)
3. run the tests with the following command:

```bash
KEYVAULT_NAME="<YOUR_KEYVAULT_NAME>" pytest -s
```

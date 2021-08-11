import os

import pytest
from azure.core.exceptions import ResourceNotFoundError
from azure.identity import DefaultAzureCredential
from azure.keyvault.secrets import SecretClient

from tests.mocks import MockedKeyVaultSecretClient

TEST_SECRETS = {
    "secret1": "Hello",
    "secret2": "World",
    "example--one": "You can't undo what's been done",
    "example--two--three": "If you can fool your friends, you can fool your enemies.",
}


def _arrange_secrets(secret_client: SecretClient):
    for key, value in TEST_SECRETS.items():
        try:
            secret = secret_client.get_secret(key)
        except ResourceNotFoundError:
            print(f"Configuring the secret: {key}...")
            secret_client.set_secret(key, value)
        else:
            if secret.value != value:
                print(f"Configuring the secret: {key}...")
                secret_client.set_secret(key, value)
            else:
                print(f"Secret {key} already configured...")


@pytest.fixture(scope="session")
def secrets_client():
    key_vault_name = os.environ.get("KEYVAULT_NAME", None)

    if key_vault_name:
        # Run real integration tests against an Azure Key Vault
        print(f"Using a real Key Vault for integration tests... {key_vault_name}")
        key_vault_url = f"https://{key_vault_name}.vault.azure.net"
        secret_client = SecretClient(
            vault_url=key_vault_url, credential=DefaultAzureCredential()
        )
        _arrange_secrets(secret_client)
    else:
        print("Using a mocked key vault secret client")
        secret_client = MockedKeyVaultSecretClient(TEST_SECRETS)

    yield secret_client

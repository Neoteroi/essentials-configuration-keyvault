from typing import Any, Dict, Iterable, Tuple

from azure.keyvault.secrets import SecretClient
from configuration.common import ConfigurationSource


class KeyVaultSource(ConfigurationSource):
    def __init__(self, client: SecretClient) -> None:
        """
        Creates a ConfigurationSource object that reads all secrets in a
        Azure Key Vault, using the given SecretClient.
        """
        super().__init__()
        self._secrets_client = client

    def normalize_secret_name(self, name: str) -> str:
        return name.replace("--", "__")

    def _list_secrets(self) -> Iterable[Tuple[str, Any]]:
        all_secrets = self._secrets_client.list_properties_of_secrets()

        for item in all_secrets:
            if item.enabled:
                secret = self._secrets_client.get_secret(item.name)
                yield self.normalize_secret_name(item.name), secret.value

    def get_values(self) -> Dict[str, Any]:
        return dict(self._list_secrets())

from dataclasses import dataclass
from typing import Dict, Iterable, Optional

from azure.keyvault.secrets import SecretClient


@dataclass
class SecretInfo:
    name: str
    enabled: bool


@dataclass
class Secret(SecretInfo):
    value: str


class MockedKeyVaultSecretClient(SecretClient):
    """
    A fake Azure Key Vault SecretClient to mock secrets.
    """

    def __init__(self, secrets: Optional[Dict[str, str]] = None) -> None:
        self._secrets = secrets or {}

    def get_secret(self, name: str) -> Secret:
        assert name in self._secrets
        return Secret(name, True, self._secrets[name])

    def list_properties_of_secrets(self) -> Iterable[SecretInfo]:
        for key in self._secrets.keys():
            yield SecretInfo(key, True)

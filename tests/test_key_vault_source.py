import pkg_resources
from azure.keyvault.secrets import SecretClient
from configuration.common import ConfigurationBuilder
from configuration.json import JSONFile

from configuration.keyvault import KeyVaultSource

from .conftest import TEST_SECRETS


def _get_file_path(file_name: str) -> str:
    return pkg_resources.resource_filename(__name__, f"./{file_name}")


def test_key_vault_source(secrets_client: SecretClient):
    builder = ConfigurationBuilder(KeyVaultSource(secrets_client))

    config = builder.build()

    assert config.secret1 == TEST_SECRETS["secret1"]
    assert config.secret2 == TEST_SECRETS["secret2"]
    assert config.example.one == TEST_SECRETS["example--one"]
    assert config.example.two.three == TEST_SECRETS["example--two--three"]


def test_key_vault_source_overriding(secrets_client: SecretClient):
    builder = ConfigurationBuilder(
        JSONFile(_get_file_path("./settings.json")),
        KeyVaultSource(secrets_client),
    )

    config = builder.build()

    assert config.test is True
    assert config.example.one == TEST_SECRETS["example--one"]
    assert config.example.two.three == TEST_SECRETS["example--two--three"]


def test_key_vault_source_overridden(secrets_client: SecretClient):
    builder = ConfigurationBuilder(
        KeyVaultSource(secrets_client),
        JSONFile(_get_file_path("./settings.json")),
    )

    config = builder.build()

    assert config.test is True
    assert config.secret1 == "Hello"
    assert config.secret2 == "World"
    assert config.example.one == "Lorem ipsum"
    assert config.example.two.three == "dolor sit amet"

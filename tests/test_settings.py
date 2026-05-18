import os


def test_env_defaults(monkeypatch):
    # Arrange
    monkeypatch.delenv("LOG_LEVEL", raising=False)

    # Import tarde para capturar monkeypatch
    # (o módulo deve ser criado pela implementação do worker)
    from reputation_api_worker.settings import get_settings

    # Act
    s = get_settings()

    # Assert
    assert s.log_level == "INFO"
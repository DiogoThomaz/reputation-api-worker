# reputation-api-worker

Worker do **Reputation API**.

## Objetivo
Processar jobs assíncronos relacionados à reputação e persistir/emitir resultados conforme regras de negócio.

## Requisitos
- GitHub Actions
- Python 3.11+
- Preferencialmente: gerenciador de dependências (ex.: poetry/uv/pip-tools)

## Ambiente e variáveis
**Regra:** variáveis de ambiente **nunca** devem ser versionadas no repositório.

### Como configurar
1. Copie o arquivo de exemplo (não versionado, apenas referência):
   - `env.example` (inclui apenas nomes/descrições, sem segredos)
2. Crie um arquivo local `.env` **fora do git**.
3. Garanta que `.env` está no `.gitignore`.

### `env.example`
Inclua apenas:
- `ENV_NAME`/`ENVIRONMENT`
- `BROKER_URL`
- `DATABASE_URL`
- `REDIS_URL` (se aplicável)
- `LOG_LEVEL`
- `SENTRY_DSN` (se aplicável)

## Testes
Rodar:
```bash
pytest -q
```

## Documentação de arquitetura
- Camada de “worker/handlers”
- Camada de “services”
- Camada de “repository/persistence”

## Segurança
- Sem segredos no código.
- Sem segredos em logs.
- Secrets devem ser injetados via GitHub Secrets.

## CI/CD
- Pipeline de testes em PRs/commits na branch `dev`.
- Deploy somente após aprovação (se houver infraestrutura definida).

from src.base.user.cli.cli import cli
from src.repository.postgres_database import PostgresDatabase
from src.repository.redis_database import RedisDatabase
from src.factories.repository_factory import RepositoryFactory

RepositoryFactory.register("postgresql", PostgresDatabase)
RepositoryFactory.register("redis", RedisDatabase)


if __name__ == "__main__":
    # uvicorn.run(
    #     "app:app",
    #     host=settings.host,
    #     port=settings.port,
    #     reload=True,
    # )
    cli()

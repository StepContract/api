up:
	docker compose up app

enter-app:
	docker compose exec app sh

enter-db:
	docker compose exec -it mariadb bash

migration-migrate:
	docker compose exec app alembic upgrade head

migration-downgrade:
	docker compose exec app alembic downgrade -1

migration-create:
	docker compose exec app alembic revision --autogenerate -m "$(msg)"

build:
	docker-compose -f docker-compose.yml build
run:
	docker-compose run alembic_vm bash
stop:
	docker-compose down
db:
	docker-compose up -d alembic_db
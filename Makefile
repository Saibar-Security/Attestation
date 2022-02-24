.PHONY: test lint run migrate

test:
	pytest -q

lint:
	ruff check .

run:
	flask --app wsgi run --port 8000

migrate:
	@for f in migrations/*.sql; do echo "applying $$f"; psql "$$DATABASE_URL" -f "$$f"; done

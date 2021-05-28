.PHONY: dev
LINE=DEPLOYMENT_CONFIG=./deployment/config/.env
FILE=.env
dev:
	grep -qFxs -- "$(LINE)" "$(FILE)" || echo "$(LINE)" >> "$(FILE)"
	docker-compose build
	docker-compose up
.PHONY: load-fixtures
FIXTURES_FILES=fixtures/*
load-fixtures:
	 docker-compose exec backend bash -c "./manage.py loaddata $(FIXTURES_FILES)"

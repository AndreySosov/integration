CONTAINER_NAME=fastapi_app
.DEFAULT_GOAL := help
build:
	@echo "Building the docker image ..."
	@docker-compose build --no-cache

up:
	@echo "Starting the docker container..."
	@docker-compose up

down:
	@echo "Stopping and removing the Docker containers..."
	@docker-compose down

logs:
	@echo "Viewing logs from Docker containers..."
	@docker-compose logs -f

test:
	@echo "Running tests..."
	@docker-compose -exec -T $(CONTAINER_NAME) pytest

myenv:
	@echo "Runing virtual environment"
	@source myenv/Scripts/activate

help:
	@echo "Makefile commands:"
	@echo "  build    - Build the Docker image with no cache."
	@echo "  up       - Build and start the Docker containers."
	@echo "  down     - Stop and remove the Docker containers."
	@echo "  logs     - View logs from Docker containers."
	@echo "  test     - Run tests inside the Docker container."
	@echo "  help     - Show this help message."
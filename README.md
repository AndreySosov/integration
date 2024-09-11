# Integration Testing Project

This project is designed for testing the integration of various tools and technologies. It uses Docker containers to set up an isolated environment where different services can work together seamlessly.

## Getting Started

### Prerequisites

Make sure you have Docker installed on your machine.
Also install the make utility in your IDE for easy command execution

### Configuration

1. Create a `.env` file in the root directory of the project with the following content:

    ```
    DB_HOST=your_database_host
    DB_PORT=your_database_port
    DB_USER=your_database_user
    DB_PASS=your_database_password
    DB_NAME=your_database_name
    ```

    Replace the placeholders with your actual database configuration.

### Running the Project

1. **Build and Start Containers**: Use the following command to create Docker images:
    ```bash
    make build
    ```

2. **Build and Start Containers**: Use the following command to build the Docker images, start the containers, apply database migrations, and start the application:

    ```bash
    make up
    ```

3. **Stop and Remove Containers**: To stop and remove all running containers, use:

    ```bash
    make down
    ```

4. **Run Tests**: If you have tests configured, run them with:

    ```bash
    make test
    ```

The `Makefile` is used to manage Docker containers and simplify common tasks such as starting, stopping, and testing the application. 

For any issues or further questions, please refer to the project's documentation or reach out to the maintainers.

Happy testing!

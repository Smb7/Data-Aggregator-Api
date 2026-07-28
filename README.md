# Data Aggregator Api
A backend application using FastAPI that concurrently fetches data from two or three public APIs (like weather, stock prices, or game server statuses) and aggregates the data into a single, cleaned-up JSON response.

## How to run locally with Docker

1.  **Build the Docker image:**
    ```bash
    docker build -t data-aggregator-api .
    ```

2.  **Run the Docker container:**
    ```bash
    docker run -p 8000:80 data-aggregator-api
    ```
    The API will be available at `http://localhost:8000`. You can access the health check at `http://localhost:8000/health` and the interactive documentation at `http://localhost:8000/docs`.

## Examples

## Skills Showcased: 
Asynchronous programming (async/await), third-party API integration, data parsing, and high-performance Python web frameworks.

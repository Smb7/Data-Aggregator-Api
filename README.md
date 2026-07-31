# Data Aggregator Api
A high-performance backend application using FastAPI that concurrently fetches and standardizes user profile data from multiple mocked gaming platforms (Steam, Xbox Live, and Riot Games) into a single, unified JSON response.

## Skills Showcased: 
Asynchronous programming (async/await), third-party API integration, data parsing, and high-performance Python web frameworks.

## How to run locally with Docker
1. **Clone repository**
    ```bash
    git clone https://github.com/Smb7/Data-Aggregator-Api.git
    ```

1. **Navigate to project directory**
    ```bash
    cd Data-Aggregator-Api
    ```

3.  **Build the Docker image:**
    ```bash
    docker build -t data-aggregator-api .
    ```

4.  **Run the Docker container:**
    ```bash
    docker run -p 8000:80 data-aggregator-api
    ```
    The API will be available at `http://localhost:8000`. You can access the health check at `http://localhost:8000/health` and the interactive documentation at `http://localhost:8000/docs`.

**Delete the Docker image:**
    ```bash
    docker rmi -f data-aggregator-api
    ```

## API Documentation

Access the interactive API documentation (Swagger UI) at:
http://localhost:8000/docs

## Example API Call

You can test the `/profile/{gamer_tag}` endpoint using `curl`:

```bash
curl -X GET "http://localhost:8000/profile/test_user" -H "accept: application/json"

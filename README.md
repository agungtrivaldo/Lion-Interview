# Retail ETL with Airflow & PostgreSQL

ETL pipeline for retail transactions using Apache Airflow, PostgreSQL, and Docker.

## Features

ETL pipeline for retail transactions
Dockerized setup with separate OLTP, DWH, and Airflow containers
Airflow DAGs for scheduled ETL jobs
Persistent storage using Docker volumes
Airflow Web UI for monitoring DAGs

## Project Structure

airflow/
├── dags/ # Airflow DAGs and ETL scripts
├── logs/ # Airflow logs
docker-compose.yml # Docker Compose configuration
Dockerfile.airflow # Custom Airflow image
README.md # Project documentation
volumes/
├── oltp/ # OLTP DB persistent data
├── dwh/ # DWH DB persistent data
└── airflow/ # Airflow DB persistent data

## Setup Instructions

### 1 Prerequisites
Docker ≥ 20.x
Docker Compose ≥ 1.29.x
Python ≥ 3.10 (optional, for DAG development)


### 2 Run Containers
docker-compose up -d

### 3 Access Databases
OLTP DB
Host: localhost
Port: 5432
DB: oltp_db
User: oltp_user
Password: oltp_pass

Data Warehouse (DWH)

Host: localhost
Port: 5433
DB: dwh_db
User: dwh_user
Password: dwh_pass

Airflow Metadata DB

Host: postgres_airflow
Port: 5432
DB: airflow_db
User: airflow_user
Password: airflow_pass

### 4 Access Airflow Web UI
URL: http://localhost:8081
Username: admin
Password: admin

## Notes
Docker volumes persist data between container restarts
Ensure ports 5432, 5433, 8081 are free before starting
Airflow uses LocalExecutor and a Fernet key for encryption
Image Blur Detection & Description API

# REST API for image blur detection and generating image descriptions using Google Gemini.

## Features
Image blur detection and description generation
Batch image processing and CSV export
Dockerized setup with persistent storage
FastAPI-based REST API

## Project Structure
number_2_image_api/
├── app/
│ └── main.py # FastAPI main script
├── dataset/ # Folder to store input images
├── output/ # Folder to store CSV summary
├── Dockerfile # Docker configuration
└── requirements.txt # Python dependencies

## Setup Instructions

### 1 Prerequisites
Docker ≥ 20.x
Python ≥ 3.11 (optional, for local testing)
Gemini API key (for generating image descriptions)

### 2 Build Docker Image
cd number_2_image_api
docker build -t image_api .

#### Build Docker Compose (if you want to make in other vm or pc)
services:
  api:
    image: agung/image-api:latest
    ports:
      - "8000:8000"
    volumes:
      - ./images:/app/images
    environment:
      - GEMINI_API_KEY=&{GEMINI_API_KEY}

### 4 Run Docker Compose
docker compose up -d

### 5 Access API
Endpoint: http://localhost:8000/blur_detect
Send POST request with JSON payload:
{
"image_url": "http://localhost/dataset/sample.jpg"
}

Response:

If blurred: { "result": "blur" }

If not blurred: { "result": "<description from Gemini>" }

### 6 Batch Processing & CSV Export
python app/main.py --batch --output output/summary.csv
Processes all images in dataset/
Saves results to output/summary.csv

## Notes
Docker volumes ensure dataset and output persist between container restarts
Gemini API key must be exported as environment variable
requirements.txt includes all dependencies (fastapi, uvicorn, opencv-python, requests, openai, pandas)
Create a new docker compose if using other vm 
    services:
    api:
        image: agung/image-api:latest
        ports:
        - "8000:8000"
        volumes:
        - ./images:/app/images
        environment:
        - GEMINI_API_KEY=&{GEMINI_API_KEY}
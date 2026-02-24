# FastAPI Iris Prediction API

**Live Demo (Cloud Run):** https://your-service-name.a.run.app/docs

A simple machine learning API that predicts Iris flower species using a trained scikit-learn model.

## Features
- FastAPI backend with automatic Swagger/OpenAPI docs
- POST /predict endpoint for batch/single predictions
- Dockerized for easy local & cloud deployment
- Ready for Google Cloud Run (serverless)

## Tech Stack
- Python 3.11+
- FastAPI
- scikit-learn & joblib
- Uvicorn
- Docker

## Quick Start (Local)
```bash
docker build -t iris-api .
docker run -p 8080:8080 iris-api
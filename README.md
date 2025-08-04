# Hotel Reservation Prediction with MLFlow, Jenkins and GCP Deployment

## Table of Contents
- 📌 [Project Overview](#project-overview)
- 📊 [Architecture](#architecture)
- ⚙️ [Tech Stack](#tech-stack)
- 🔄 [CI/CD Pipeline Stages](#ci-cd-pipeline-stages)
- 📊[Project Workflow](#project-workflow)
- 🔄[Model Deployment](#model-deployment)
- 📝 [Future Enhancements](#future-enhancements)
-  [Dataset](#dataset)

## 📌 Project Overview

This project aims to help hotels manage their bookings more effectively by predicting potential reservation cancellations. It provides a user-friendly interface for hotel managers, along with backend automation to streamline the ML lifecycle from data ingestion to deployment.

**Key Objectives:**
- Predict cancellations using historical data
- Improve hotel revenue with overbooking strategies
- Enable targeted marketing to reduce cancellations
- Detect fraudulent booking behaviors

## Architecture
On every code push to GitHub, Jenkins triggers an automated pipeline that builds a Docker image, pushes it to Google Container Registry, and deploys it to Google Cloud Run.
This ensures continuous integration and seamless deployment without manual intervention.

<img width="6594" height="591" alt="image" src="https://github.com/user-attachments/assets/5b140cf7-4057-44a7-a019-9a14de76c475" />

## Teck Stack

| Layer                   | Technology Used                         |
| ----------------------- | --------------------------------------- |
| **Data Storage**        | GCS (Google Cloud Storage)              |
| **ML Dev**              | Python, Pandas, Sklearn, Jupyter        |
| **Experiment Tracking** | MLflow                                  |
| **App Backend**         | Flask                                   |
| **Frontend**            | HTML/CSS                                |
| **Containerization**    | Docker                                  |
| **CI/CD**               | Jenkins, GitHub                         |
| **Deployment**          | Google Cloud Run                        |
| **Data & Code Versioning**          | GitHub |


## CI/CD Pipeline Stages

- **Code push**: Developer pushes updated code/model to GitHub.
- **Jenkins trigger**: Automatically starts Jenkins pipeline on Puch code to GitHub.
- **Build phase**: Jenkins:
    - Pulls code
    - Creates Docker image
- **Push to GCR**: Docker image is pushed to Google Container Registry.
- **Deployment**: Jenkins deploys the image to Google Cloud Run.
- **Live App**: Application is available on the internet with a public URL.

## Project Workflow
1. Database Setup
Upload the hotel reservation dataset (CSV) to a Google Cloud Storage (GCP Bucket) to simulate real-world cloud-based data storage.

2. Project Initialization
- Set up a clean Python project structure with:
- Virtual environment
- Logging system
- Custom exceptions
- Config files for scalable development

3. Data Ingestion
Programmatically download data from the GCP bucket into your local project directory and split it into train/test sets for modeling.

4. Jupyter Testing
Perform EDA, data preprocessing, model selection, and validation in a Jupyter Notebook to establish a blueprint for the final pipeline code.

5. Model Training
Convert the notebook logic into structured Python scripts using classes and functions, ensuring reusable and production-ready code.

6. Experiment Tracking
- Use MLflow to track:
- Metrics (accuracy, precision, etc.)
- Model versions
- Hyperparameters
- Artifacts (trained models)

7. Pipeline Integration
Combine data ingestion, preprocessing, and model training into a single training pipeline script for automated execution.

8. Version Control
- Use GitHub for code versioning.
- Use DVC for data versioning if dataset size grows in future.

9. User App
Build a Flask-based web interface for hotel staff to input booking data and receive cancellation predictions without writing any code.

10. CI/CD Automation
- Set up a Jenkins pipeline to automate:
    - Docker image creation
    - Pushing to Google Container Registry (GCR)
    - Deployment to Google Cloud Run for live access

## Model Deployment


## Future Enhancements
- Integrate Grafana & Prometheus for monitoring
- Support Kubernetes (GKE) deployment for scaling
- Implement feature engineering automation
- Add user authentication to the Flask app
- Create ETL pipelines with Apache Airflow
- Enhance UI using React or Streamlit for richer UX

## Dataset

[Hotel Reservation Dataset on Kaggle](https://www.kaggle.com/datasets/ahsan81/hotel-reservations-classification-dataset)
  

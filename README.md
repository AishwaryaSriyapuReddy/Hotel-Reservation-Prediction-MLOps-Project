# Hotel Reservation Prediction with MLFlow, Jenkins and GCP Deployment

## Table of Contents
- 📌 [Project Overview](#project-overview)
- 📊 [Architecture](#architecture)
- ⚙️ [Tech Stack](#tech-stack)
- 🔄 [CI/CD Pipeline Stages](#ci-cd-pipeline-stages)
- 📊[Project Workflow](#project-workflow)
- 🧪 [CircleCI Pipeline Testing](#circleci-pipeline-testing)
- 🔄[Model Deployment](#model-deployment)
- 📝 [Future Enhancements](#future-enhancements)

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

<img width="6999" height="591" alt="image" src="https://github.com/user-attachments/assets/ef307055-164c-4a14-a7cb-6c7036dae67b" />


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

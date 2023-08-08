# GCP-Containerized-Microservices
Containerized Microservices with GCP: Build, deploy, and manage containerized microservices for a professional application using Google Cloud Platform (GCP). The application involves user registration, login validation, online user tracking, and interaction. Utilize Firestore as the backend database for efficient data storage and retrieval.


## Overview

This repository hosts a professionally developed containerized microservices application on Google Cloud Platform (GCP). The application encompasses user registration, login validation, online user tracking, and interaction. Firestore, GCP's database service, is utilized to store and manage user data.

### Features

- **Containerized Microservices:** Three distinct containerized microservices designed for different backend functionalities.
- **User Registration:** Accept registration details from the frontend and store them in the Firestore database.
- **Login Validation:** Validate user login information by comparing with the backend database.
- **Online User Tracking:** Maintain and display user states (online, offline) on the frontend in real-time.
- **Session Management:** Maintain user sessions from login to logout, updating the Firestore database accordingly.
- **Deployment:** Build Docker images, push them to GCP's Artifact Registry, and deploy the containers using Cloud Run.

### Web Pages
Three simple web pages are developed to interact with the microservices. These pages facilitate user registration, login, and display online user states.

### Testing
Thorough testing of the application has been conducted, including:
- Unit tests for individual microservices.
- End-to-end testing for user registration, login, and online user tracking.

### Technology Stack
- Google Cloud Run: Deploy and manage containerized applications.
- Firestore: Cloud-based NoSQL database for efficient data storage.
- Docker: Containerization for easy deployment and scalability.
- Artifact Registry: Repository for storing Docker container images.

---

## How to Use

1. Clone this repository: `git clone <repository_url>`
2. Explore and modify microservices code as needed.
3. Build Docker images for each microservice and push them to GCP's Artifact Registry.
4. Deploy the containerized microservices using Google Cloud Run.
5. Access the web pages to interact with the application.
6. Test the application thoroughly and ensure proper functionality.

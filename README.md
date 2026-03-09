# Microservice-App
# Random Color Microservice App

## Project Overview

This is a **simple microservice-style application** built for learning container concepts.

The application has two parts:

* **Frontend** → A simple web page with a button
* **Backend** → A Python service that returns a random color

When the user clicks the button on the frontend, the frontend calls the backend API and the page background changes to a **random color**.

This project is useful to demonstrate:

* Containers
* Frontend–Backend communication
* Podman containers
* Podman Pods
* Podman Compose

---

# Project Structure

```
color-app
│
├── backend
│     ├── app.py
│     └── Containerfile
│
└── frontend
      ├── index.html
      └── Containerfile
```

**backend/**
Contains the Python API that returns a random color.

**frontend/**
Contains a simple webpage that calls the backend and changes the background color.

---

# How the Application Works

1. User opens the web page.
2. User clicks the **Change Color** button.
3. Frontend sends a request to the backend.
4. Backend generates a **random color**.
5. Frontend receives the color and changes the page background.

Architecture:

```
Browser
   │
   │ 8080
   ▼
Frontend (nginx)
   │
   │ API request
   ▼
Backend (python)
   │
random color
```

---

# Build Container Images

Go to the project directory and build the images.

Build backend image:

```
podman build -t color-backend ./backend
```

Build frontend image:

```
podman build -t color-frontend ./frontend
```

Check images:

```
podman images
```

---

# Run Containers

Run backend container:

```
podman run -d -p 5000:5000 color-backend
```

Run frontend container:

```
podman run -d -p 8080:80 color-frontend
```

---

# Test the Application

Open a browser and go to:

```
http://localhost:8080
```

Click the **Change Color** button.

The page background will change to a random color.

---

# Learning Purpose

This project helps understand:

* How frontend and backend services communicate
* How to build container images
* How to run containers using Podman
* How a simple microservice application works

Later this same project can also be used to demonstrate:

* **Podman Pods**
* **Podman Compose**
* **Kubernetes YAML (podman play kube)**

---

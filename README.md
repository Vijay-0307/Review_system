# Product Reviews with Streamlit and MongoDB Atlas

This project is a simple application built with Streamlit and MongoDB Atlas that allows users to submit and view product reviews.

## Setup Instructions

1. Clone this repository to your local machine.
2. Ensure Python and pip are installed.
3. Install the required packages:

   ```bash
   pip install -r requirements.txt

   ```bash
   python scripts/setup_db.py

4. Start the Streamlit application:

   ```bash
   streamlit run streamlit_app.py

## Table of Contents

- [Introduction](#introduction)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [MongoDB Atlas Setup](#mongodb-atlas-setup)
  - [Creating a MongoDB Atlas Cluster](#creating-a-mongodb-atlas-cluster)
  - [Connecting to the Cluster](#connecting-to-the-cluster)
  - [Setting Up the Database](#setting-up-the-database)
- [Setting Up the Environment](#setting-up-the-environment)
  - [Python Installation](#python-installation)
  - [Streamlit Installation](#streamlit-installation)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [Customization](#customization)
- [License](#license)

## Introduction

This project is a simple product review application that allows users to submit reviews and view the latest reviews in near real-time. The front-end is built using Streamlit, and the back-end uses MongoDB Atlas to store the reviews.

## Technologies Used

- **Streamlit**: A framework for creating interactive data applications.
- **MongoDB Atlas**: A cloud-based MongoDB database service.
- **Python**: The programming language used for both front-end and back-end.
- **pymongo**: A Python library to interact with MongoDB databases.

## Project Structure

- `streamlit_app.py`: The main Streamlit application file.
- `scripts/setup_db.py`: A script for setting up the MongoDB collection and initializing with sample data.
- `data/initial_reviews.json`: Contains sample reviews for initial database setup.
- `requirements.txt`: Lists required Python packages for the project.
- `README.md`: This document.
- `.streamlit/config.toml`: Streamlit configuration file (optional).

## MongoDB Atlas Setup

To use MongoDB Atlas, you need to create a cluster, set up a database, and obtain the connection string.

### Creating a MongoDB Atlas Cluster

1. Sign up for a free account at [MongoDB Atlas](https://www.mongodb.com/cloud/atlas).
2. Create a new cluster. You can choose a free tier for small projects.
3. Select your cloud provider and region.
4. Click "Create Cluster."

### Connecting to the Cluster

1. Once your cluster is created, go to the "Connect" button.
2. Choose "Connect Your Application."
3. Copy the connection string and replace the placeholder with your actual username and password.

### Setting Up the Database

1. After connecting to your cluster, create a new database.
2. Create a collection named `reviews`.
3. You can also use `scripts/setup_db.py` to create the collection and insert initial reviews.

## Setting Up the Environment

### Python Installation

Ensure Python is installed on your system. You can download the latest version from [Python.org](https://www.python.org/downloads/).

### Streamlit Installation

To install Streamlit, run the following command:

```bash
pip install streamlit


### Guidelines

These setup instructions in the README file provide a detailed guide for setting up and running your Streamlit application. It covers cloning the repository, setting up the MongoDB connection, installing Python dependencies, running a database setup script, starting the Streamlit app, and accessing it through a web browser. Additionally, there's a section on common issues and troubleshooting for resolving common problems.

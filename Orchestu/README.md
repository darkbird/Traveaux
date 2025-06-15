# Orchestu - AI Agent SaaS Platform

Orchestu is a platform designed for the creation, management, and orchestration of AI agents. It aims to provide robust tools for automation (including n8n integration), quality assurance, role management, and seamless API connectivity.

## Project Status - Phase 1 Complete

This project has completed its initial development phase (Phase 1). This phase focused on establishing the foundational backend and frontend structures, creating placeholder implementations for key services, and setting up the development environment. Many backend services currently use in-memory data storage, and integrations are simulated. The frontend primarily uses mock data.

## Project Structure

The `Orchestu` project is organized into the following main directories:

-   `/backend`: Contains the Flask (Python) backend application.
    -   `/auth`: User authentication and authorization.
    -   `/connectors`: Integration with external APIs (currently simulated).
    -   `/integrations`: Connectors for services like n8n (currently simulated).
    -   `/orchestration`: Logic for agent task orchestration (currently simulated).
    -   `/quality_assurance`: Endpoints for agent quality data (in-memory).
    -   `models.py`, `routes.py`, `app.py`: Core agent management and application setup.
-   `/frontend`: Contains the React (Vite) frontend application.
    -   `/src/components`: Reusable UI components.
    -   `/src/App.jsx`: Main application component.
-   `/database`: (Placeholder) Intended for database schema, migrations, etc. Contains a `.gitkeep` file.
-   `/docs`: (Placeholder) Intended for detailed documentation. Contains a `.gitkeep` file.
-   `/tests`: (Placeholder) Intended for backend and frontend tests. Contains a `.gitkeep` file.

## Getting Started

### Backend

The backend is a Flask application.
-   **Dependencies**: Ensure Python 3.x is installed. Install dependencies:
    ```bash
    cd Orchestu/backend
    pip install -r requirements.txt
    ```
-   **Running the Backend**:
    ```bash
    cd Orchestu/backend
    python app.py
    ```
    The backend server will typically start on `http://localhost:5000`.

### Frontend

The frontend is a React application built with Vite.
-   **Dependencies**: Ensure Node.js and npm are installed. Install dependencies:
    ```bash
    cd Orchestu/frontend
    npm install
    ```
-   **Running the Frontend**:
    ```bash
    cd Orchestu/frontend
    npm run dev
    ```
    The frontend development server will typically start on `http://localhost:5173` (or another port indicated by Vite).

## Next Steps / Future Development

Future development will focus on:

-   **Database Integration**: Transitioning backend services from in-memory storage to a persistent database (e.g., PostgreSQL, MongoDB).
-   **Full Service Implementation**:
    -   Implementing real API calls in `/connectors` and `/integrations/n8n_connector`.
    -   Developing the orchestration engine beyond simulation.
    -   Building out comprehensive quality metric calculations and storage.
-   **Enhanced Frontend**:
    -   Connecting frontend components to live backend APIs.
    -   Building UIs for agent creation, orchestration flow design, user management, and quality monitoring.
-   **Testing**: Adding comprehensive unit, integration, and end-to-end tests.
-   **Deployment**: Defining and implementing a deployment strategy for both backend and frontend.
-   **Real-time Features**: Exploring real-time communication for agent status and logs (e.g., WebSockets).

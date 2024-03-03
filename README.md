# CS Messaging Web App

Welcome to the CS Messaging Web App project! This project aims to provide a simple messaging web application for Branch that can scale with the growing customer base, allowing agents to respond to incoming messages from customers in a streamlined fashion.

## Features

- Allows multiple agents to log in simultaneously and respond to incoming messages.
- Supports sending and receiving messages through an API endpoint.
- Provides a portal for agents to view and respond to customer messages.
- Stores messages in a database for easy retrieval and management.

## Technologies Used

- Python (Flask) for backend development
- React for frontend development
- SQLite for database storage

## Application Structure

The application follows a client-server architecture, with the following components:

- `frontend/`: Contains files related to the user interface.
- `backend/`: Holds server-side logic for routing and handling requests.
- `database/`: Stores the SQLite database for messages.

## Setup Instructions

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Set up a virtual environment (optional but recommended).
4. Install dependencies by running `pip install -r requirements.txt`.
5. Run the Flask application by executing `python backend/app.py`.
6. Access the application in your browser at `http://localhost:5000`.

## Usage

1. Log in to the application as an agent.
2. View incoming messages from customers.
3. Select a message to respond to.
4. Compose and send a response.
5. Repeat the process to handle more messages.

## Deployment

You can deploy the application to a cloud platform like Heroku or AWS for production use. Make sure to update the database connection string accordingly.

## Maintenance

- Regularly backup the database to prevent data loss.
- Monitor application performance and error logs.
- Keep dependencies updated to their latest versions.
- Document code changes and update documentation as needed.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

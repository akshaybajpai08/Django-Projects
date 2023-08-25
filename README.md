# Django Employee Chat Room

The Django Employee Chat Room is a web application designed to facilitate real-time communication among employees within an organization. This platform allows employees to engage in group discussions, one-on-one conversations, and share important updates seamlessly.

![Chat Room Screenshot](screenshot.png)

## Features

- **User Authentication:** Employees can create accounts and log in securely to access the chat room.
- **Real-Time Messaging:** Users can send and receive messages instantly, making communication efficient.
- **Group Chats:** Employees can participate in group conversations based on teams, projects, or specific topics.
- **Private Messaging:** Users can also have private conversations with their colleagues for confidential discussions.
- **Message Notifications:** Receive notifications for new messages, even when the browser is minimized.
- **User Status:** See the online/offline status of colleagues for better availability management.
- **Emojis and Attachments:** Express emotions using emojis and share files for better collaboration.
- **Responsive Design:** The application is responsive and works seamlessly across different devices.
- **Admin Dashboard:** Administrators can manage users, monitor chats, and ensure smooth operation.

## Installation

1. Clone this repository: `git clone https://github.com/yourusername/django-employee-chat-room.git`
2. Navigate to the project directory: `cd django-employee-chat-room`
3. Create a virtual environment: `python -m venv venv`
4. Activate the virtual environment: `source venv/bin/activate` (Linux/macOS) or `venv\Scripts\activate` (Windows)
5. Install dependencies: `pip install -r requirements.txt`
6. Apply migrations: `python manage.py migrate`
7. Run the development server: `python manage.py runserver`

Visit `http://127.0.0.1:8000/` in your web browser to access the chat room.

## Technologies Used

- Django: Backend framework for building robust web applications.
- Django Channels: Enables real-time communication through WebSockets.
- JavaScript/jQuery: Enhances user interactions and handles real-time updates.
- HTML/CSS: Frontend design and layout.

## Contributions

Contributions are welcome! If you'd like to contribute to this project, please follow the guidelines in [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to fork, modify, and use this project according to your needs. If you find any issues or have suggestions for improvements, please open an issue or a pull request. Happy coding!


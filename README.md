# Django Chatbot

A conversational chatbot built with Django and ChatterBot, designed to provide interactive responses using natural language processing.

## Features

- **Conversational AI**: Powered by ChatterBot for natural language understanding
- **Django Backend**: Robust web framework for handling requests and responses
- **SQLite Database**: Default database for storing conversation data
- **NLTK Integration**: For natural language processing capabilities
- **Admin Interface**: Built-in Django admin for managing chatbot responses

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Chatbot
   ```

2. **Create and activate a virtual environment** (recommended)
   ```bash
   python -m venv venv
   .\venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply database migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser (optional, for admin access)**
   ```bash
   python manage.py createsuperuser
   ```

## Running the Application

1. **Start the development server**
   ```bash
   python manage.py runserver
   ```

2. **Access the application**
   - Chat interface: http://127.0.0.1:8000/
   - Admin interface: http://127.0.0.1:8000/admin/

## Project Structure

```
Chatbot/
├── chatcli/              # Django project configuration
├── chatcliapp/           # Main application
├── manage.py             # Django management script
├── db.sqlite3            # SQLite database (created after first run)
└── requirements.txt      # Project dependencies
```

## Dependencies

- Django 4.2.x
- ChatterBot2 1.0.4
- NLTK 3.8.1
- SQLAlchemy 1.3.24
- pytz

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Django](https://www.djangoproject.com/)
- Powered by [ChatterBot](https://github.com/gunthercox/ChatterBot)
- Natural Language Processing with [NLTK](https://www.nltk.org/)

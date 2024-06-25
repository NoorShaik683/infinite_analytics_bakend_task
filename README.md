# Picnic Planner Application

[Demo Video](https://github.com/NoorShaik683/infinite_analytics_bakend_task/assets/106299708/1aac666f-06c3-4428-9a92-96a56f1c685e)


## Technologies Used
- **Python 3.x**
- **Django 3.x**: Python web framework
- **PostgreSQL**: Relational database for storing application data
- **HTML/CSS**: Frontend templates for rendering user interface
- **Open-Meteo API**: Third-party API for fetching weather data

## Installation and Setup

### Prerequisites
- Python 3.x installed on your machine/server
- PostgreSQL database server
- Virtual environment (optional but recommended)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/NoorShaik683/infinite_analytics_bakend_task
   cd infinite_analytics_bakend_task
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Database setup**
   - Create a PostgreSQL database and note down the credentials.
   - Update `settings.py` with your database settings:
     ```python
     DATABASES = {
         'default': {
             'ENGINE': 'django.db.backends.postgresql',
             'NAME': 'your_database_name',
             'USER': 'your_database_user',
             'PASSWORD': 'your_database_password',
             'HOST': 'localhost',
             'PORT': '5432',
         }
     }
     ```

4. **Apply migrations**
   ```bash
   python manage.py migrate
   ```

5. **Load initial data (optional)**
   - I have created a management command to add some dummy data into tables.
   ```bash
   python manage.py populate_data
   ```

### Running the Application

1. **Start the Django development server**
   ```bash
   python manage.py runserver
   ```

2. **Access the application**
   Open a web browser and go to `http://localhost:8000` to view the Picnic Planner application.

### Usage

- **Home Page**: Lists available locations.
- **Location Details Page**: Displays picnic spots for a selected location with current weather information.
- **Subscribe**: Allows users to subscribe for weather updates at their chosen location and time slot.

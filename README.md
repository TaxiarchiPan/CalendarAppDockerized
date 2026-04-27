
# Cloud-Ready Calendar App 

## A modern and dedicated event management system that organizes your schedule.
 Project Structuredocker-compose.yaml: Service orchestration and environment settings.web/app.py: Flask API routes and database connection logic.web/static/: Contains the style.css and script.js that power the UI.web/templates/index.html: The main structure of the calendar application.
## Features

* **Interactive Calendar Interface** – Navigate months and years with an automated "today" focus.

* **Persistent Event Storage** – Add, view, and delete events that stay saved in a MySQL 8.0 database.

* **Cloud & Docker Ready** – Fully containerized architecture using Docker Compose for instant deployment.

* **Minimalist & Aesthetic UI** – Features a clean design with the Poppins font and a smooth, user-friendly interface.

## Technical Stack

**Frontend**: HTML5, CSS3, and JavaScript.

**Backend**: Python 3.9 powered by Flask 2.3.2.

**Database**: MySQL for robust data persistence.

**Infrastructure**: Docker & Docker Compose.

## Run Locally

Clone the project

```bash
  git clone https://github.com/TaxiarchiPan/CalendarAppDockerized.git
```

Go to the project directory

```bash
  cd calendar_app_cloud
```

Launch the application:


```bash
  docker-compose up --build
```

Access the interface: Open your browser and navigate to:

```bash
  http://localhost:5200
```


## Project Structure 

* **docker-compose.yaml:** Service orchestration and environment settings.

* **web/app.py:** Flask API routes and database connection logic.

* **web/static/:** Contains the style.css and script.js that power the UI.

* **web/templates/index.html:** The main structure of the calendar application.


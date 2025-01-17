
Air Quality Prediction in Smart Cities Using Machine Learning

This project aims to predict air quality levels in smart cities using machine learning techniques. It provides a web-based interface to visualize air pollution data and forecast trends, aiding in environmental analysis and decision-making.
---
## Features
- **Air Quality Prediction:** Machine learning models to forecast air quality indices.
- **Data Visualization:** Interactive charts displaying historical air pollution data.
- **Web Interface:** A Django-based application for user interaction.
- **Database Integration:** Uses SQLite for managing data.
---
## Project Structure
- **`.vscode/`**: IDE-specific configuration files.
- **`air/`** and **`AirPollution/`**: Modules or packages for air quality prediction.
- **`db.sqlite3`**: SQLite database file for storing application data.
- **`finalyear_project/`**: Core Django project files.
- **`manage.py`**: Script for Django project management.
- **`model/`**: Contains machine learning models or related assets.
- **`myapp/`**: Main Django application folder.
- **`requirements.txt`**: Python dependencies required for the project.
- **`static/`**: Contains CSS, JavaScript, and other static assets.
- **`templates/`**: HTML templates for rendering web pages.
---
## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Raghu050/Air-Quality-Prediction-in-Smart-Cities.git
   cd Air-Quality-Prediction-in-Smart-Cities
   ```
2. **Set Up a Virtual Environment:**
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Apply Migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Run the Development Server:**
   ```bash
   python manage.py runserver
   ```
6. **Access the Application:**
   Open a browser and navigate to `http://127.0.0.1:8000/`.
---
## Usage
- Visualize air pollution data across various cities.
- Predict future air quality trends.
- Explore insights through interactive charts and tables.
---
## Technologies Used
- **Back-End:** Django, SQLite
- **Front-End:** HTML, CSS, JavaScript (Chart.js)
- **Machine Learning:** Python libraries (details in `model/` directory)
- **Version Control:** Git
---
## Contributions
Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.
---
## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
---
## Acknowledgments
Special thanks to the team members and mentors who contributed to this project.

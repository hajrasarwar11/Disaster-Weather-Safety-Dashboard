# **Disaster & Weather Safety Dashboard**

## **Project Overview**
The **Disaster & Weather Safety Dashboard** is a Python application that aggregates data from multiple public APIs to provide users with up-to-date weather alerts and recent earthquake information. This project demonstrates the concept of a **Federated Data Aggregator (FDA)**, which combines data from distinct sources into a unified, meaningful report.

By entering latitude and longitude coordinates, users can instantly see:
- Current weather conditions at the specified location.
- A list of recent earthquakes globally, including magnitude and location.

This project highlights **object-oriented design, API integration, secure configuration management, and robust error handling**.

---

## **Features**
- Fetches live weather data using the **OpenWeatherMap API**.  
- Fetches recent earthquake data using the **USGS Earthquake API**.  
- Combines results into a single, user-friendly report.  
- Handles invalid inputs, network errors, and API failures gracefully.  
- Logs program events and errors using Python's `logging` module.  

---

## **Installation**

### **1. Clone the repository**
git clone <repository-url>  
cd Disaster_Weather_Aggregator  

### **2. Set up a virtual environment (optional but recommended)**
python -m venv .venv

### **3. Activate the virtual environment**
For Windows:  
.venv\Scripts\activate

### **4. Install dependencies**
pip install -r requirements.txt

### **5. API Key Setup**
Create a .env file at the root of the project (you can copy from .env.example):  
OPENWEATHER_API_KEY=your_api_key_here  
Replace your_api_key_here with your actual OpenWeatherMap API key.  

You can get a free key from OpenWeatherMap.  

Ensure the .env file is not committed to version control for security reasons.  

## **Running the Application**
Run the main program using the terminal:   
python main.py  
Enter the latitude and longitude when prompted.  

The program will fetch weather and earthquake data and display a combined report.  

Example Output:   
=== Disaster & Weather Safety Dashboard ===  
Enter latitude: 33.6844  
Enter longitude: 73.0479  

--- Weather Alerts ---  
- Weather: Clouds (few clouds), Temp: 25°C  

--- Recent Earthquakes ---  
- M 4.5 - South of Lombok, Indonesia  
- M 3.9 - 33 km NNW of Eagle, Alaska  
...  

## **Project Structure**
Disaster_Weather_Aggregator/  
│  
├── clients/  
│   ├── base_client.py  
│   ├── weather_alert_client.py  
│   └── earthquake_client.py  
│  
├── aggregator.py         # Combines API results into a unified report  
├── logger.py             # Handles logging for errors/events  
├── main.py               # Main program; runs the system  
├── requirements.txt  
├── .env.example          # Template for API keys  
└── README.md  

## **Logging**
All errors, exceptions, and key events are logged using logger.py to:  
Help debug issues  
Record user inputs and program activity  
Maintain an audit trail of API calls  
Log output is stored in app.log and optionally displayed on the console.  

## **Notes**
Ensure your internet connection is active to fetch data from APIs.  
Latitude and longitude must be valid numeric values.  
This project follows PEP 8 coding standards and uses OOP principles for maintainability and scalability.  

## **License**
This project is for educational purposes under the MIT License.  

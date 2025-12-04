from aggregator import DataAggregator
from logger import logging

def main():
    logging.info("=== Disaster & Weather Safety Dashboard Started ===")

    # Get user input
    try:
        latitude = float(input("Enter latitude: "))
        longitude = float(input("Enter longitude: "))
        logging.info(f"User entered coordinates: latitude={latitude}, longitude={longitude}")
    except ValueError:
        logging.error("Invalid input! User did not enter valid numeric coordinates.")
        print("Invalid input! Please enter valid numeric coordinates.")
        return

    # Create aggregator
    aggregator = DataAggregator()
    report = aggregator.get_combined_report(latitude, longitude)
    logging.info("Combined report fetched successfully.")

    # Display Weather Alerts
    print("\n--- Weather Alerts ---")
    weather_alerts = report.get("Weather Alerts", [])
    if not weather_alerts:
        logging.info("No weather alerts found for this location.")
        print("No weather alerts at this location.")
    else:
        for alert in weather_alerts:
            print(f"- {alert}")  # alert is now a string like "Weather: Clear (clear sky), Temp: 22°C"
            logging.info(f"Weather alert displayed: {alert}")

    # Display Recent Earthquakes
    print("\n--- Recent Earthquakes ---")
    earthquakes = report.get("Recent Earthquakes", [])
    if not earthquakes:
        logging.info("No recent earthquakes found for this location.")
        print("No recent earthquakes.")
    else:
        for eq in earthquakes:
            props = eq.get("properties", {})
            mag = props.get("mag", "N/A")
            place = props.get("place", "Unknown location")
            print(f"- M {mag} - {place}")
            logging.info(f"Earthquake displayed: M {mag} - {place}")

if __name__ == "__main__":
    main()

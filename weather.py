import requests

class Clime:
    def __init__(self, city="Tucuman"):
        self.city = city
        self.key = "c41f962f29e04fcab0d171915240108"
        self.url = "http://api.weatherapi.com/v1/current.json?key="+self.key+"&q="+self.city+"&aqi=no"
        self.raw = None
        self.data = None
        self.forecasted = None
        self.fetch_data()

    def fetch_data(self):
        """Fetch weather data from the API."""
        try:
            self.raw = requests.get(self.url)
            self.raw.raise_for_status()
            self.data = self.raw.json()
            self.forecasted = self.data["current"]
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data: {e}")
            self.raw = None
            self.data = None
            self.forecasted = None

    def check_api(self):
        """Check if the API request was successful."""
        return self.raw is not None and self.raw.ok

    def get_location(self):
        """Return location data."""
        if self.data:
            return self.data.get("location")
        return None

    def get_temperature(self):
        """Return the current temperature in Celsius."""
        if self.check_api():
            return self.forecasted.get("temp_c")
        return None

    def get_humidity(self):
        """Return the current humidity percentage."""
        if self.check_api():
            return self.forecasted.get("humidity")
        return None

    def get_icon(self):
        """Return the URL of the weather icon."""
        if self.check_api():
            condition = self.forecasted.get("condition")
            if condition:
                filtered_icon = {key: condition[key] for key in ['text', 'icon']}
                return filtered_icon
        return None

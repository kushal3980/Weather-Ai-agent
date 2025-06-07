from smolagents import CodeAgent, HfApiModel, tool, GradioUI


@tool
def get_weather_data(city: str) -> dict:
    """Fetches weather data for a given city.
    
    Args:
        city (str): The name of the city to fetch weather data for. yes 
    """

    # sampple data for demonstration purposes
    sample_data = {
        "new york": {
            "temps": [72, 75, 65, 68, 70, 74, 73],
            "rain": [0, 0.2, 0.5, 0, 0, 0.1, 0],
            "unit": "F"
        },
        "london": {
            "temps": [15, 14, 16, 13, 15, 17, 16],
            "rain": [0.5, 0.2, 0, 0.1, 0.3, 0, 0.2],
            "unit": "C"
        },
        "tokyo": {
            "temps": [22, 24, 23, 25, 26, 25, 22],
            "rain": [0, 0, 0.3, 0.2, 0, 0, 0.1],
            "unit": "C"
        }
    }

    city_lower = city.lower()
    return sample_data.get(city_lower, {"error": f"No data for {city}"})


model = HfApiModel()
agent = CodeAgent(tools=[get_weather_data], model=model, additional_authorized_imports=["matplotlib.pyplot"], verbosity_level=2)

# run the agent with a query
print("Running agent with weather query...")
# response = agent.run('''
# Get the weather data for New York.
# 1. calculate the average temperature
# 2. calculate the rainy days
# 3. plot the temperature and rain data
# 4. save the chart as 'weather_chart.png' (dont use plt.show())
                     
#                      ''')

GradioUI(agent).launch()

import requests
import pandas as pd
import time
import random

# Initialize an empty list to store scraped data
res = []

# Set user agent and headers
headers = {
    'authority': 'www.swiggy.com',
    '__fetch_req__': 'true',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.7',
    'content-type': 'application/json',
    'dnt': '1',
    'if-none-match': 'W/"a456-nwr2WlfwUHrV5BaSCsSNhpFkTJ4"',
    'referer': 'https://www.swiggy.com/',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'user-agent': 'Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
}

# Set initial parameters
params = {
    'lat': '15.4027005',
    'lng': '74.00778489999999',
    'offset': '0',
    'sortBy': 'DELIVERY_TIME',
    'page_type': 'DESKTOP_SEE_ALL_LISTING'
}

while True:
    # URL with parameters
    url = f'https://www.swiggy.com/dapi/restaurants/list/v5?lat={params["lat"]}&lng={params["lng"]}&offset={params["offset"]}&sortBy={params["sortBy"]}&page_type={params["page_type"]}'
    
    # Make a request to Swiggy
    response = requests.get(url, headers=headers)

    try:
        # Extract data from the response
        data = response.json()['data']['cards']
    except (KeyError, IndexError):
        break

    for i in range(15):
        try:
            card_data = data[i]['data']['data']

            # Skip if the restaurant is not opened
            if 'opened' in card_data and card_data['opened'] == False:
                continue

            # Create a dictionary to store relevant information
            row = {}
            for key in ['id', 'name', 'area', 'address', 'locality', 'totalRatingsString', 'costForTwoString', 'city', 'veg']:
                row[key] = card_data.get(key)

            res.append(row)

        except (KeyError, IndexError):
            # Stop the loop if 'data' or 'cards' keys are missing
            break
        
        if len(res) >= 5000:
            break

    # Stop the loop if there are no more results available or reached the limit
    if not data or len(res) >= 5000:
        break

    # Update the offset for the next iteration
    params['offset'] = str(int(params['offset']) + 15)

    # Sleep for a random amount of time between 1 and 5 seconds to avoid overwhelming the server
    time.sleep(random.uniform(1, 3))

# Create a DataFrame from the collected data
df = pd.DataFrame(res)

# Define the output file path
output_file_path = 'path_to_your_file.csv'

# Save the DataFrame to a CSV file
df.to_csv(output_file_path, index=False)

# Print the DataFrame
print(df)
print(f'Data saved to: {output_file_path}')

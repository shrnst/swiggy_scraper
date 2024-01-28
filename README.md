# Swiggy Scraper

This script allows you to scrape restaurant data from Swiggy based on location parameters. 

## Usage

1. **Find Latitude and Longitude:** Visit the [Swiggy website](https://www.swiggy.com/) to find the latitude and longitude of your desired area.

2. **Customize Parameters:** Update the parameters in the script to match your preferences.

3. **Run the Script:** Execute the script to initiate the scraping process.

## Customizable Parameters

- `lat`: Latitude of the location
- `lng`: Longitude of the location
- `offset`: Offset for pagination
- `sortBy`: Sorting criteria for the restaurant list
- `page_type`: Type of page (e.g., 'DESKTOP_SEE_ALL_LISTING')

## Dependencies

- `requests`
- `pandas`

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json
import time

# Define the URL and the data to be inserted
url = "https://testpages.herokuapp.com/styled/tag/dynamic-table.html"
data_insert = [
    {"name": "Bob", "age": 20, "gender": "male"},
    {"name": "George", "age": 42, "gender": "male"},
    {"name": "Sara", "age": 42, "gender": "female"},
    {"name": "Conor", "age": 40, "gender": "male"},
    {"name": "Jennifer", "age": 42, "gender": "female"}
]
def validate_data(url,data_insert):
    # Convert data to JSON string
    json_data = json.dumps(data_insert)
    
    # Initialize the WebDriver 
    driver = webdriver.Chrome()  
    
    try:
        # Step 1: Navigate to the URL
        driver.get(url)
    
        # Step 2: Click on the "Table Data" button
        driver.find_element(By.XPATH, "//summary[normalize-space()='Table Data']").click()
            
        # Wait for the input box to be displayed
        time.sleep(2) 
    
        # Step 3: clear the existing data
        driver.find_element(By.XPATH, "//textarea[@id='jsondata']").clear()
                    
        # Step 4: send the data
        driver.find_element(By.XPATH, "//textarea[@id='jsondata']").send_keys(json_data)
            
        # Click on "Refresh Table" button
        driver.find_element(By.XPATH, "//button[@id='refreshtable']").click()
    
        # Step 4: Wait for the table to refresh
        time.sleep(3)  
    
        # Step 5: Assert the data in the UI table
        rows = driver.find_elements(By.XPATH, "//table[@id='dynamictable']//tr")
        
        # Extract data from the UI table
        populated_data = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            
            # Ensure there are enough cells in the row
            if len(cells) >= 3:
                populated_data.append({
                    "name": cells[0].text,
                    "age": int(cells[1].text),
                    "gender": cells[2].text
                })
               
        # Comparison
        assert populated_data == data_insert, f"Data does not match! Expected: {data_to_insert}, Found: {populated_data}"
        print("Data matched successfully!")
    
    finally:
        # Close the driver
        driver.quit()

## calling of function
validate_data(url,data_insert)
# Data Provider of Asset Crawlers Database

## Crawl Ticket from ETLE System and API to Inquiry the Result

### Project Overview:
1.	Engineer required to build crawler engine to automated checking process of ticket- (tilang) from ETLE (Electronic Traffic Law Enforcement) system and store the results checking to databases where the data can be used by others application through API
2.	Analytics want to create dashboard to view status e-tilang of customer asset

### Standards:
- Database used to store the data should be PostgreSQL, MySQL, other Open sources RDBMS 
- Crawler Engine should be developing by Python (free to use any library or services as long as it’s open sources)
- API should be creating in Python (free to use any framework e.g. Flask, FastAPI, etc.)

### Objectives:
- Create database in PostgreSQL or MySQL to store the data of check results
- Create crawler Engine using Python to automate checking process to the sources (ETLE)
- Create API to enable checking result data can be consumed by other application 
- Create table to view status e-tilang of customer asset (result from test-1)
- Archive all codes files in repository (free to use any repository e.g. GitHub, GitLab, etc.) 

### Outline the Architecture of the solution:
![Data Provider of Asset Crawlers](/3-test-answer/asset/test-2-design.drawio.png "Data Provider of Asset Crawlers")

### Outline the steps/plan of the solution:
1. When the user were requesting a data from the API, it will check in the database whether the data exist or not, if not then execute the Crawler base on the input to the Source
2. In the same Python file with the Crawler, there is also a function to Load the data to the database.
3. The data later on can be use and view in the Database and also can be use from an API to get any data that already being stored.
4. The API will bridging between the User, Crawler and Database to view the data through semi-structured format data such as JSON.

### List down the requirement/tasks required:
- **Prerequisites**
    1. **Python 3.7+**
        - Create a Python environment:
            - _python -m venv env-bfi_
        - Activate environment:
            - _source env-bfi/bin/activate_
        - Install Libraries:
            - _pip install -r 3-test-answer/src/requirements.txt_
        - Install Playwright browser driver and dependencies
            - _playwright install_ 
            - _playwright install-deps_
    2. **Docker**
        - Run PostgreSQL:
            - _docker run -itd -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=your-password -p 5432:5432 -v /your-mountpoint/pg-data:/var/lib/postgresql/data --name postgresql postgres_
        - Connect PostgreSQL using Database Management Studio(e.g DBeaver)
            - _New Database Connection => Choose PostgreSQL => Insert host/ip, port, and the credentials(username&pass)_
        - Create table for customer asset:
            - _create table customer_asset_new (no_plat varchar(255), no_mesin varchar(255), no_rangka varchar(255), waktu varchar(255), lokasi varchar(255), tipe_pelanggaran varchar(255), status varchar(255))_

### Record your notes/project here:
# Web Scraping API Documentation

This API allows you to scrape data from a website by providing the vehicle information (license plate, engine number, and chassis number). It checks if the data already exists in a PostgreSQL database and returns the existing data if found. If the data is not found, it scrapes the website and inserts the scraped data into the database

## Base URL

`http://localhost:8000`

## Endpoints

### `POST /scrape_website`

Scrapes data from the website based on the provided vehicle information

**Request Body**

- `no_plat` (string): License plate number of the vehicle
- `no_mesin` (string): Engine number of the vehicle
- `no_rangka` (string): Chassis number of the vehicle

**Response**

- If the data is already present in the database, the response will be the existing data in the following format:

  ```json
  {
    "no_plat": "A1492RH",
    "no_mesin": "4A91GD9541",
    "no_rangka": "MK2NCWHANJJ018193",
    "waktu": "29-09-2021 15:40",
    "lokasi": "Jalan Veteran Kota Serang",
    "tipe_pelanggaran": "Tidak menggunakan sabuk pengaman",
    "status": "Terbayar"
  }
- If the data is not found in the database, the response will be the scraped data in the same format

## How to Use
1. Make sure you have Python and the required libraries installed (fastapi, uvicorn, playwright, beautifulsoup4, psycopg2, and pydantic)

2. Create a PostgreSQL database and set the connection details (host, port, database, username, and password) in the code

3. Copy the provided code into a Python file (e.g., scraping_api.py)

4. Run the FastAPI application using the following command:

    ```bash
    uvicorn 3-test-answer.src.bfi_crawler:app --reload
    ```
5. The API will be available at http://localhost:8000

### Summarize what you learned:

- What did you learn?
    - The code demonstrates how to use FastAPI to create an API endpoint that accepts POST requests and interacts with a PostgreSQL database. It utilizes Playwright for web scraping and Beautiful Soup for parsing HTML data. The code also showcases the use of Pydantic for data validation and modeling.

- What worked well?
    - The code successfully scrapes the target website for car record information, inserts the data into a PostgreSQL database, and retrieves existing data if it already exists in the database

- What was the most challenging aspect of this project?
    - One of the challenges may be handling different scenarios when interacting with the website and the database. Error handling and ensuring the code works correctly in all possible cases can be a complex task

- What will you do differently next time?
    - In future iterations, I could consider implementing additional features such as authentication and authorization for the API, implementing caching mechanisms to improve performance, and addin error handling and logging to provide more detailed information about potential issues.
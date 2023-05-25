from fastapi import FastAPI
from pydantic import BaseModel
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import psycopg2

app = FastAPI()

class CustomerAssetNew(BaseModel):
    no_plat: str
    no_mesin: str
    no_rangka: str
    waktu: str
    lokasi: str
    tipe_pelanggaran: str
    status: str

# Database connection details
host = 'localhost'
port = 5432
database = 'postgres'
username = 'postgres'
password = 'password'

@app.post("/scrape_website", response_model=CustomerAssetNew)
def scrape_website(no_plat: str, no_mesin: str, no_rangka: str):
    existing_data = get_existing_data(no_plat, no_mesin, no_rangka)
    if existing_data:
        return existing_data

    input_data = {
        'no_plat': no_plat,
        'no_mesin': no_mesin,
        'no_rangka': no_rangka
    }

    result = crawl_website(input_data)
    return result

def get_existing_data(no_plat: str, no_mesin: str, no_rangka: str):
    conn = psycopg2.connect(host=host, port=port, database=database, user=username, password=password)
    cursor = conn.cursor()

    select_query = "SELECT * FROM customer_asset_new WHERE no_plat = %s AND no_mesin = %s AND no_rangka = %s"
    cursor.execute(select_query, (no_plat, no_mesin, no_rangka))

    row = cursor.fetchone()

    cursor.close()
    conn.close()

    if row:
        existing_data = {
            'no_plat': row[0],
            'no_mesin': row[1],
            'no_rangka': row[2],
            'waktu': row[3],
            'lokasi': row[4],
            'tipe_pelanggaran': row[5],
            'status': row[6]
        }
        return existing_data

    return None

def crawl_website(input_data):
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        context = browser.new_context()
        page = context.new_page()

        url = 'https://www.etlebanten.info/id/check-data'
        page.goto(url)

        page.fill('#plate', input_data['no_plat'])
        page.fill('#machineNumber', input_data['no_mesin'])
        page.fill('#skeletonNumber', input_data['no_rangka'])

        page.click('button[type="submit"]')

        page.wait_for_selector('tbody tr td.text-start')

        html_content = page.inner_html('tbody')

        browser.close()

    extracted_data = extract_data(html_content)

    combined_data = {
        'no_plat': input_data['no_plat'],
        'no_mesin': input_data['no_mesin'],
        'no_rangka': input_data['no_rangka'],
        'waktu': extracted_data[0][0],
        'lokasi': extracted_data[0][1],
        'tipe_pelanggaran': extracted_data[0][2],
        'status': extracted_data[0][3]
    }

    load_to_postgresql(combined_data)

    return combined_data

def extract_data(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    rows = soup.find_all('tr')

    extracted_data = []
    for row in rows:
        cells = row.find_all('td', class_='text-start')
        data = [cell.text.strip() for cell in cells]
        extracted_data.append(data)

    return extracted_data

def load_to_postgresql(data):
    conn = psycopg2.connect(host=host, port=port, database=database, user=username, password=password)
    cursor = conn.cursor()

    insert_query = "INSERT INTO customer_asset_new (no_plat, no_mesin, no_rangka, waktu, lokasi, tipe_pelanggaran, status) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(insert_query, (
        data['no_plat'],
        data['no_mesin'],
        data['no_rangka'],
        data['waktu'],
        data['lokasi'],
        data['tipe_pelanggaran'],
        data['status']
    ))

    conn.commit()
    cursor.close()
    conn.close()

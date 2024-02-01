import asyncio
import json

from playwright.async_api import async_playwright

async def scrape_tnstc():
    async with async_playwright() as pw:
        browser = await pw.chromium.launch(headless=True)
        page = await browser.new_page()
        url = "Your Url"
        await page.goto(url)
        route_data = {

        }

        elements = await page.query_selector_all()
        for i in elements:
            data1 = await i.inner_html()
            data2 = await i.inner_text()
            route_data.update({data2 : data1})


        # Close the browser
        await browser.close()

        # Convert data to JSON format
        json_data = dict({"data" : route_data})
        json_obj = json.dumps(json_data, indent=4)
        with open("item.json", "w") as f:
            f.writelines(json_obj)
        print("written in json")





if __name__ == '__main__':
    asyncio.run(scrape_tnstc())

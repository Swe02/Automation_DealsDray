import logging
from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Setup logging
logging.basicConfig(filename='web_interaction.log', level=logging.ERROR)

@given('I open the website "{url}"')
def step_open_website(context, url):
    try:
        context.driver = webdriver.Chrome()
        context.driver.get(f'https://www.getcalley.com/{url}')
    except Exception as e:
        logging.error(f"Error occurred while opening the website: {e}")
        raise


@step('I open the website "{url}" in mobile')
def step_open_website(context, url):
    try:
        mobile_emulation = {
            "deviceName": "iPhone X"
        }
        chrome_options = Options()
        chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

        context.driver = webdriver.Chrome(options=chrome_options)
        context.driver.get(f'https://www.getcalley.com/{url}')
    except Exception as e:
        logging.error(f"Error occurred while opening the website: {e}")
        raise

@when('I resize the window to {width:d}x{height:d}')
def step_resize_window(context, width, height):
    try:
        context.driver.set_window_size(width, height)
        size = context.driver.get_window_size()
        logging.info("Size:%s",str(size))
        assert size['width'] == width
        assert size['height'] == height
        context.driver.quit()
    except Exception as e:
        logging.error(f"Error occurred while resizing the window: {e}")
        raise



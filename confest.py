# conftest.py
import pytest
from selenium import webdriver
import os

# Your LambdaTest credentials
LT_USERNAME = os.environ.get("LT_USERNAME") or "YOUR_LAMBDATEST_USERNAME"
LT_ACCESS_KEY = os.environ.get("LT_ACCESS_KEY") or "YOUR_LAMBDATEST_ACCESS_KEY"

@pytest.fixture(params=[
    {"browserName": "chrome", "version": "latest", "platform": "Windows 10"},
    {"browserName": "safari", "version": "latest", "platform": "macOS Catalina"},
])
def driver_init(request):
    # LambdaTest capabilities
    capabilities = {
        "build": "Selenium 101 Assignment",
        "name": request.node.name, # Test name for LambdaTest dashboard
        "video": True,
        "network": True,
        "console": True,
        "visual": True, # Screenshots
        **request.param # Merge browser/OS specific capabilities
    }
    
    # LambdaTest Hub URL
    grid_url = f"https://{LT_USERNAME}:{LT_ACCESS_KEY}@hub.lambdatest.com/wd/hub"

    print(f"Starting WebDriver with capabilities: {capabilities}")
    driver = webdriver.Remote(command_executor=grid_url, desired_capabilities=capabilities)
    
    # Set implicit wait
    driver.implicitly_wait(10)
    
    yield driver
    
    # Teardown
    if driver:
        # Pass or fail the test on LambdaTest based on pytest result
        # This part requires more advanced pytest hooks or a custom finalizer
        # For simplicity, we'll just quit the driver here, but in a real scenario
        # you'd update LambdaTest test status.
        driver.quit()

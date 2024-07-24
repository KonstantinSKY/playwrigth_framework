import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from .utils import navigate_and_wait  # Ensure this import statement is correct

# Fixture to navigate to the page and wait for it to load
@pytest.fixture(scope="session")
def page(context):
    page = context.new_page()
    navigate_and_wait(page, "https://testpages.eviltester.com/styled/basic-html-form-test.html")
    yield page
    page.close()


# Test functions using the pre-loaded page fixture
def test_example_page_title(page):
    # Check if the title contains "Example Domain"
    expect(page).to_have_title(" HTML Form Elements")
    
    # title = page.locator("title")
    # assert title.text_content() == " HTML Form Elements"

def test_example_page_heading(page):
    # Check if the heading is present
    heading = page.locator("h1")
    
    expect(heading).to_have_text("Basic HTML Form Example")
    assert heading.text_content() == "Basic HTML Form Example"
    
    expect(heading).to_be_visible()
    assert heading.is_visible() == True

    if heading.count() > 0:
        print("Element is present")
    else:
        print("Element is not present")


# def test_fill_username(page):
#     # Fill the username field
#     username_input = page.locator("input[name='username']")
#     username_input.click()
#     # Optional delay after clicking the field
#     page.wait_for_timeout(5000)
#     username_input.fill("testuser")
#     page.wait_for_timeout(5000)
#     # Optionally, you can add assertions here
#     expect(username_input).to_have_value("testuser")


def test_dropdown(page):

    options_to_test = ['Selection Item 1', 'Drop Down Item 2', 'Selection Item 3', 'Selection Item 4']
    dropdown_selector = 'select[name="dropdown"]'
    dropdown_locator = page.locator('select[name="dropdown"]')
    dropdown_locator.scroll_into_view_if_needed()
    bounding_box = dropdown_locator.bounding_box()

    
    if bounding_box:
            # Move the mouse to the option and click
        page.mouse.move(bounding_box['x'] + bounding_box['width'] / 2, bounding_box['y'] + bounding_box['height'] / 2)
        print("OK MOVED")
        page.wait_for_timeout(2000)
        page.mouse.click(bounding_box['x'] + bounding_box['width'] / 2, bounding_box['y'] + bounding_box['height'] / 2)
        print("OK CLICKED")
        page.wait_for_timeout(2000)
    # dropdown_locator.click()
    page.wait_for_timeout(1000)
    # page.select_option(dropdown_selector, 'Drop Down Item 1')
    # page.wait_for_timeout(5000)
    # dropdown_locator.press("ArrowDown")
    # page.wait_for_timeout(1000)
    # dropdown_locator.press("ArrowDown")
    # page.wait_for_timeout(1000)
    # dropdown_locator.press("Enter")

    page.wait_for_timeout(1000)

    option_text = 'Drop Down Item 2'
    # option_locator = page.locator(f'select[name="dropdown"] >> text={option_text}')
    option_locator = page.locator(f'option[value="dd2"]')
    # option_locator = dropdown_locator.locator(option_selector);
    print("Count:", option_locator.count(), option_locator)

    # option_value = 'dd2'  # Replace with the desired option value
    # page.evaluate(f'''
    #         var option = document.querySelector('select[name="dropdown"] option[value="{option_value}"]');
    #         option.style.display = 'block';
    #         option.style.visibility = 'visible';
        # ''')
    # option_locator.scroll_into_view_if_needed()
    # option_locator.wait_for(state='visible')
    # option_locator.wait_for(state='attached')
    # option_locator.wait_for(state='stable')
    
    bounding_box = option_locator.bounding_box()
    if bounding_box:
        page.mouse.move(bounding_box['x'] + bounding_box['width'] / 2, bounding_box['y'] + bounding_box['height'] / 2)
        print("OK 222MOVED")
        page.wait_for_timeout(2000)
        page.mouse.click(bounding_box['x'] + bounding_box['width'] / 2, bounding_box['y'] + bounding_box['height'] / 2)
        print("OK 222CLICKED")
    
    
    # option_locator = page.locator(f'select[name="dropdown"] option', has_text=option_text)
    # Ensure the option is visible
    # option_locator.scroll_into_view_if_needed()
    # bounding_box = option_locator.bounding_box()
 # Get the bounding box of the option
    # bounding_box = dropdown_locator.bounding_box()
    
    # if bounding_box:
    #         # Move the mouse to the option and click
    #     page.mouse.move(bounding_box['x'] + bounding_box['width'] / 2, bounding_box['y'] + bounding_box['height'] / 2)
    #     page.mouse.click(bounding_box['x'] + bounding_box['width'] / 2, bounding_box['y'] + bounding_box['height'] / 2)
    #     # Physically click on the option
    # # option_locator.click()

    # # option_value = 'dd4'
    # # page.select_option(dropdown_selector, option_value)
    # # page.click(option_selector)
    # page.wait_for_timeout(5000)
    
    # # Verify the selection by checking the selected value
    # selected_option = page.query_selector(f'{dropdown_selector} option:checked').get_attribute('value');
    
    # print("Selected Options", selected_option);
    # selected_option_locator = dropdown_locator.locator('option:checked')
    # selected_option = selected_option_locator.inner_text().strip()
    # assert selected_option == option_text, f"Expected 'Drop Down Item 2' but got '{selected_option}'"
    # page.click(selected_option)

    page.wait_for_timeout(5000)
       # Locate the button
    # button = page.locator("button")
    
    # Method 1: Using expect
    # expect(button).to_have_text("Click Me")    
    
    # # Check if the "More information..." link is present and visible
    # more_info_link = page.locator("a", has_text="More information...")
    # expect(more_info_link).to_be_visible()
    
    # # Click the "More information..." link
    # more_info_link.click()
    
    # Perform any additional actions or assertions as needed


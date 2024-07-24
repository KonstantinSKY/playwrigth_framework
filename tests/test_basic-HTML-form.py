import pytest
from playwright.sync_api import Playwright, sync_playwright, expect
from .utils import navigate_and_wait  # Ensure this import statement is correct


# Fixture to navigate to the page and wait for it to load
@pytest.fixture(scope="session")
def page(context):
    page = context.new_page()
    navigate_and_wait(
        page, "https://testpages.eviltester.com/styled/basic-html-form-test.html"
    )
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

    options_to_test = [
        "Drop Down Item 1",
        "Drop Down Item 2",
        "Drop Down Item 3",
        "Drop Down Item 4",
    ]
    dropdown_selector = 'select[name="dropdown"]'
    dropdown_locator = page.locator(dropdown_selector)

    option_selector = f"option, has_text={options_to_test[1]}"
    option_locator = dropdown_locator.locator(option_selector)

    assert dropdown_locator.is_visible(), "Dropdown is not visible."
    assert dropdown_locator.is_enabled(), "Dropdown is not enabled."
    dropdown_locator.scroll_into_view_if_needed()

    page.wait_for_timeout(1000)
    # dropdown_locator.click()
    # Find the option with partial text
    option_locator = dropdown_locator.locator(
        f'option:has-text("{options_to_test[1]}")'
    )
    print(f"Locator for {options_to_test[1]}: {option_locator}")
    option_value = option_locator.get_attribute("value")


    print(f"Option with partial text '{options_to_test[1]}' has value: {option_value}")
    dropdown_locator.select_option(option_value)

    page.wait_for_timeout(1000)
    selected_option_locator = dropdown_locator.locator("option:checked")
    selected_option_text = selected_option_locator.inner_text().strip()
    print("Selected options by text:", selected_option_text)
    assert (
        selected_option_text == options_to_test[1]
    ), f"Expected '{options_to_test[1]}' but got '{selected_option_text}'"

    selected_option_value = selected_option_locator.get_attribute('value')
    print("Selected options by value:", selected_option_value)
    assert (
        selected_option_value == option_value
    ), f"Expected '{option_value}' but got '{selected_option_value}'"

    # dropdown_locator.select_option(label = " Drop Down Item 2 ")

    page.wait_for_timeout(1000)
    # Print all options for debugging
    all_options = dropdown_locator.locator("option")
    all_options_count = all_options.count()
    print(f"Total options in dropdown: {all_options_count}")
    # Print all options for debugging
    all_options = dropdown_locator.locator("option")
    print("All options in dropdown:")
    for i in range(all_options.count()):
        print(
            all_options.nth(i).get_attribute("value"),
            all_options.nth(i).inner_text().strip(),
        )

        # assert all_options.nth(i).is_visible(), f"Option {all_options.nth(i).inner_text().strip()} not visible"
        # assert all_options.nth(i).is_enabled(), f"Option {all_options.nth(i).inner_text().strip()} not enabled"

    page.wait_for_timeout(1000)

    # option_to_select = options_to_test[2]
    # print(f"Attempting to select option: {option_to_select}")

    #     # Select the option
    # try:
    #     dropdown_locator.select_option(label=option_to_select)
    #     print(f"Selected option: {option_to_select}")
    # except Exception as e:
    #     print(f"Failed to select option: {e}")
    #     raise
    # page.wait_for_timeout(5000)
    # dropdown_locator.click()
    # page.wait_for_timeout(1000)
    # Verify the selection

    # selected_option_locator = dropdown_locator.locator('option:checked')
    # selected_option = selected_option_locator.inner_text().strip()
    # print("Selected options:", selected_option)
    # assert selected_option == option_to_select, f"Expected '{options_to_test[2]}' but got '{selected_option}'"
    # page.wait_for_timeout(1000)
    # # bounding_box = dropdown_locator.bounding_box()

    # if bounding_box:
    #         # Move the mouse to the option and click by
    #     page.mouse.move(bounding_box['x'] + bounding_box['width'] / 2, bounding_box['y'] + bounding_box['height'] / 2)
    #     print("OK MOVED")
    #     page.wait_for_timeout(2000)
    #     page.mouse.click(bounding_box['x'] + bounding_box['width'] / 2, bounding_box['y'] + bounding_box['height'] / 2)
    #     print("OK CLICKED")
    #     page.wait_for_timeout(2000)
    # # dropdown_locator.click()
    # page.wait_for_timeout(1000)
    # page.select_option(dropdown_selector, 'Drop Down Item 1')
    # page.wait_for_timeout(5000)
    # dropdown_locator.press("ArrowDown")
    # page.wait_for_timeout(1000)
    # dropdown_locator.press("ArrowDown")
    # page.wait_for_timeout(1000)
    # dropdown_locator.press("Enter")

    # page.wait_for_timeout(1000)

    # option_text = 'Drop Down Item 2'
    # # option_locator = page.locator(f'select[name="dropdown"] >> text={option_text}')
    # option_locator = page.locator(f'option[value="dd2"]')
    # # option_locator = dropdown_locator.locator(option_selector);
    # print("Count:", option_locator.count(), option_locator)

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

    # bounding_box = option_locator.bounding_box()
    # if bounding_box:
    #     page.mouse.move(bounding_box['x'] + bounding_box['width'] / 2, bounding_box['y'] + bounding_box['height'] / 2)
    #     print("OK 222MOVED")
    #     page.wait_for_timeout(2000)
    #     page.mouse.click(bounding_box['x'] + bounding_box['width'] / 2, bounding_box['y'] + bounding_box['height'] / 2)
    #     print("OK 222CLICKED")

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

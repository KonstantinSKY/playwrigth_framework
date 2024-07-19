import pytest
from playwright.sync_api import Playwright, sync_playwright, expect

# Global variable to track fatal errors
FATAL_ERROR = False

def test_1() -> None:
    """
    A test that passes.
    """
    assert 1 == 1
    assert 2 == 2
    assert 3 == 3

@pytest.mark.xfail
def test_2() -> None:
    """
    A test that is expected to fail.
    """
    assert 1 == 1
    assert 2 == 2
    assert 1 == 2 + 4 - 8  # This will fail

def test_3() -> None:
    """
    A test that fails partway through and continues with the remaining steps.
    """
    assert 1 == 1
    print("STEP continue :0")
    assert 1 == 2  # This will fail
    # Code below will not run because of the previous failure
    print("STEP continue :1")
    assert 1 == 1
    print("STEP continue :2")
    assert 2 == 2

def test_4() -> None:
    """
    A test that collects multiple failures and fails at the end.
    """
    errors = []

    # Zero assert
    print("\nSTEP continue :0")
    step_0_passed = (1 == 2)
    if not step_0_passed:
        print("TEST FAIL Assertion 0 Error")
        errors.append("Assertion 0 failed")

    # First assert
    print("STEP continue :1")
    step_1_passed = (1 == 2)
    if not step_1_passed:
        print("TEST FAIL Assertion 1 Error")
        errors.append("Assertion 1 failed")

    # Second assert
    print("STEP continue :2")
    step_2_passed = (2 == 5)
    if not step_2_passed:
        print("TEST FAIL Assertion 2 Error")
        errors.append("Assertion 2 failed")

    # Third assert
    print("STEP continue :3")
    step_3_passed = (3 == 3)
    if not step_3_passed:
        print("TEST FAIL Assertion 3 Error")
        errors.append("Assertion 3 failed")

    # If there were any errors, fail the test at the end
    if errors:
        pytest.fail("; ".join(errors))

def test_5() -> None:
    """
    A test that passes with a warning message.
    """
    assert 1 == 1
    assert 2 == 2
    try:
        assert 1 == 2  # This will fail but is caught as a warning
    except AssertionError as e:
        print(" Warning Assertion 2 Error: ", e)
    assert 2 == 2
    assert 1 == 1

def test_6() -> None:
    """
    A test that sets a fatal error flag and stops further tests if a failure occurs.
    """
    global FATAL_ERROR
    print("STEP continue :1")
    assert 1 == 1

    try:
        assert 1 == 2  # This will fail and set the fatal error flag
    except AssertionError:
        FATAL_ERROR = True
        pytest.fail("Failure.")

    print("Continuing after failure.")
    # The following lines will not execute if the above fail triggers exit
    print("This code runs after the second failure.")
    print("STEP continue :3")
    assert 1 == 1
    print("STEP continue :4")
    assert 2 == 1
    print("STEP continue :5")
    assert 1 == 4

def fatal_stop():
    """
    Stops the test suite if a fatal error has been detected.
    """
    global FATAL_ERROR
    if FATAL_ERROR:
        pytest.exit("FATAL ERROR detected, stopping further tests.", 1)

def test_7() -> None:
    """
    A test that checks for fatal errors before running.
    """
    fatal_stop()
    print("STEP 1 just for checking")
    assert 1 == 1
    assert 2 == 1  # This will fail if it runs, but shouldn't if fatal_stop is triggered

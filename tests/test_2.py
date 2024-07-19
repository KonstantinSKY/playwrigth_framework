import pytest
from playwright.sync_api import Playwright, sync_playwright, expect


# def test_1() -> None: # Pass

#     assert 1 == 1
#     assert 2 == 2
#     assert 3 == 3
# # assert text
# # expect(1).toBe(1)
# # expect(1).toBe(1)
# # expect(1).toBe(1)


# @pytest.mark.xfail
# def test_2() -> None: # Fail manually

# # expect(1).toBe(1)
# # expect(1).toBe(1)
# # expect(1).toBe(1)
#     assert 1 == 1
#     assert 2 == 2
#     assert 1 == 2 + 4 - 8
# # Push to Fail


# def test_3() -> None: # Fail
# # # Fail and Stop test3 and continue with next tests
#     assert 1 == 1
#     print("STEP continue :0")
#     assert 1 == 2
#  # Fail and Stop test3 and continue with next tests
#     print("STEP continue :1")
#     assert 1 == 1
#     print("STEP continue :2")
#     assert 2 == 2


# def test_4() -> None:  # Fail
#     errors = []

#     # Fail the test and continue with next steps

#     # Zero assert
#     print("\nSTEP continue :0")
#     step_0_passed = (1 == 2)
#     if not step_0_passed:
#         print("TEST FAIL Assertion 0 Error")
#         errors.append("Assertion 0 failed")

#     # First assert
#     print("STEP continue :1")
#     step_1_passed = (1 == 2)
#     if not step_1_passed:
#         print("TEST FAIL Assertion 1 Error")
#         errors.append("Assertion 1 failed")


#     # Second assert
#     print("STEP continue :2")
#     step_2_passed = (2 == 5)
#     if not step_2_passed:
#         print("TEST FAIL Assertion 2 Error")
#         errors.append("Assertion 2 failed")


#     # Third assert
#     print("STEP continue :3")
#     step_3_passed = (3 == 3)
#     if not step_3_passed:
#         print("TEST FAIL Assertion 3 Error")
#         errors.append("Assertion 3 failed")

#     # If there were any errors, fail the test at the end
#     if errors:
#         pytest.fail("; ".join(errors))


# #
# def test_5() -> None: # Pass

#     assert 1 == 1
#     assert 2 == 2
#     try:
#         assert 1 == 2
# # much code
#     except AssertionError as e:
# # much code
#         print(" Warning Assertion 2 Error: ", e)

# # # Pass the step and continue with next steps. This is when we just pass a warning message and continue

# assert 1 == 1


def test_6() -> None: # Fail
    print("STEP continue :1")
    assert 1 == 1

# Fail and Stop test execution
# Stop Program
    print("STEP continue :1!!! FATAL ERROR TEST")
    try:
        assert 1 == 2, "Fatal Error"
# much code
    except AssertionError as e:
        print("STEP FAILED:", e)
        pytest.fail("FATAL ERROR WITH PYTEST EXIT", pytrace=False)
        pytest.exit("FATAL ERROR WITH PYTEST EXIT", returncode=1)
        print("EXIT IS NOT OK!!!!!!!!!!!!!!!!")
        exit(0);
# 0 - exit without an error
# 1 exit with the error
    print("STEP continue :3")
    assert 1 == 1
    print("STEP continue :4")
    assert 2 == 1


#Just for checking EXITING 
def test_7() -> None: # Pass
    print("STEP 1 just for checking")
    assert 1 == 1
    assert 2 == 1

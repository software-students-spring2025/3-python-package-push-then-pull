import pytest
# from popmessage import popmsg

class Tests:
    
    @pytest.fixture
    def example_fixture(self):
        """
        An example of a pytest fixture - a function that can be used for setup and teardown before and after test functions are run.
        """

        # place any setup you want to do before any test function that uses this fixture is run

        yield  # at the yield point, the test function will run and do its business

        # place with any teardown you want to do after any test function that uses this fixture has completed

    # @pytest.fixture
    # def popup(self):
    #     """Fixture to create a new PopupMessage instance before each test"""
    #     popup_instance = popmsg.PopupMessage()
    #     return popup_instance
        
    # Test functions
    def test_sanity_check(self, example_fixture):
        """
        Test debugging... making sure that we can run a simple test that always passes.
        Note the use of the example_fixture in the parameter list - any setup and teardown in that fixture will be run before and after this test function executes
        From the main project directory, run the `python3 -m pytest` command to run all tests.
        """
        expected = True  # the value we expect to be present
        actual = True  # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"

    # def test_initializations(self, popup):
    #     assert popup._message == "Default Message"
    #     assert popup._bgColor == "white"
    #     assert popup._fontColor == "black"
    #     assert popup._fontSize == 75
    #     assert popup._timerDuration == 0
    #     assert popup._type == popmsg.PopupMessage.POPUP_TYPE_REGULAR
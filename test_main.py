from main import astro
from main import readings


def test_astro():
    """ 
    A unit test to see if text is written to a file
    """

    TEST_TEXT = "Here is some text"
    TEST_FILENAME = "filename.out"

    astro(TEST_TEXT, TEST_FILENAME)

    with open(TEST_FILENAME) as file:
        lines = file.readlines()
        final_line = lines[-1]

    assert final_line == TEST_TEXT
    #os.remove(TEST_FILENAME)

# def test_astro():
#     """ 
#     A unit test to see if a file is created
#     """
#     TEST_TEXT = "test"
#     TEST_FILENAME = "file_name.out"

#     text_to_file(TEST_TEXT, TEST_FILENAME)

#     assert TEST_FILENAME in os.listdir()
#     os.remove(TEST_FILENAME)
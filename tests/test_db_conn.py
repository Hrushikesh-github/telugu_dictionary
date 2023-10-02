import logging

def test_db_word(test_db):
    response = test_db.query_meanings_for_word('గాణ')
    # Assertion will fail for wrong words or failed DB connection
    assert response != None
    logging.info(f"the meaning we got is: {response}")


def test_import():
    from dbwarden_seeds import setup
    assert callable(setup)

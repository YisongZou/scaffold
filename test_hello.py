from hello import add, main


def test_add():
    assert add(1, 2) == 3
    assert add(3, 4) == 7
    main()

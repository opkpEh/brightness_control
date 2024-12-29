from src.screen_dimmer import main

def test_about_flag(monkeypatch, capsys):
    monkeypatch.setattr('sys.platform', 'win32')
    monkeypatch.setattr('sys.argv', ['__main__.py', '--about'])

    main()

    captured = capsys.readouterr()
    expected_output= "Take your brightness level to beyond its limits!\n"

    assert captured.out == expected_output
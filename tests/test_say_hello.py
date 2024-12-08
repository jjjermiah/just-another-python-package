import pytest
from just_another_python_package.main import hello, main;


def test_say_hello():
    assert hello() == (
        "Hello from just_another_python_package, [bold magenta]World[/bold magenta]!", ":vampire:"
    )

def test_main(capsys):
    """Test the main function."""
    main()
    captured = capsys.readouterr()
    assert "just_another_python_package" in captured.out
    assert "World" in captured.out
    assert "🧛" in captured.out

if __name__ == "__main__":
    pytest.main()

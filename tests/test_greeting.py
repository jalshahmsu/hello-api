from hello_api.greeting import build_greeting


def test_build_greeting_uses_given_name() -> None:
    assert build_greeting("JS") == "Hello, JS!"

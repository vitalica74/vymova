from frontend.text_processing import normalize_text, tokenize_text

def test_normalize():
    assert normalize_text("  Привіт   світе  ") == "Привіт світе"

def test_tokenize():
    assert tokenize_text("Привіт світ") == ["Привіт", "світ"]

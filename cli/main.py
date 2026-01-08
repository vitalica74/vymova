from frontend.text_processing import tokenize_text

def main():
    import sys
    text = " ".join(sys.argv[1:])
    tokens = tokenize_text(text)
    print("Tokens:", tokens)


if __name__ == "__main__":
    main()

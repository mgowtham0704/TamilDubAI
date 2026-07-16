from deep_translator import GoogleTranslator


def translate_to_tamil(text):
    tamil = GoogleTranslator(
        source="auto",
        target="ta"
    ).translate(text)

    return tamil
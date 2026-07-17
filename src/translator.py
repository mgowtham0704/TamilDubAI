import logging

from deep_translator import GoogleTranslator

logger = logging.getLogger(__name__)


def translate_to_tamil(text):
    """
    Translate text to Tamil.
    """
    try:
        logger.info("Translating text to Tamil...")

        tamil = GoogleTranslator(
            source="auto",
            target="ta"
        ).translate(text)

        return tamil

    except Exception:
        logger.exception("Translation failed.")
        raise
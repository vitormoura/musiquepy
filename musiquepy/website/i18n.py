import gettext
import os

# pybabel extract --input-dirs ./musiquepy/website   -o ./musiquepy/website/messages.pot --project 'musiquepy.website' --version 1.0.0
# pybabel init -i .\musiquepy\website\messages.pot -d .\musiquepy\website\locales\ -l pt
# pybabel update -i .\musiquepy\website\messages.pot -d .\musiquepy\website\locales\ -l fr
# pybabel compile -d .\musiquepy\website\locales\ --use-fuzzy

_locales_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'locales'
)

_messages_index = {
    'en': gettext.translation('messages', _locales_path, languages=['en'], fallback=True),
    'fr': gettext.translation('messages', _locales_path, languages=['fr'], fallback=True),
    'pt': gettext.translation('messages', _locales_path, languages=['pt'], fallback=True)
}
_messages = _messages_index['en']


def _(msg: str) -> str:
    return _messages.gettext(msg)


def set_lang(locale):
    global _messages

    _messages = _messages_index[locale]

class Locale:
    def __init__(self, lang):
        self.lang = lang
        self.message = self.setMessages(lang)
    def setMessages(self, lang):
        if lang == 'ru':
            return self.ruLang()
        elif lang == 'en':
            return self.enLang()
    def ruLang(self):
        return {
            'greeting': 'Да здраствуй, здраствуй.',
            'unknow-mes': 'Я не врубаюсь, что ты говоришь.',
            'lang-error': 'Чтобы переключить язык, введите /lang [код языка (ru, en и т.д.)]',
            'setup-lang': 'Язык установлен на: Русский'
        }
    def enLang(self):
        return {
            'greeting': 'Hello hello.',
            'unknow-mes': 'I don\'t understand what you say.',
            'lang-error': 'To switch the languagem, enter /lang [language code (ru, en, etc.)]',
            'setup-lang': 'Language is set to: English'
        }
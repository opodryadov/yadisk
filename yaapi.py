import requests
import yadisk
#  документация https://yandex.ru/dev/translate/doc/dg/reference/translate-docpage/

API_KEY = 'trnsl.1.1.20190712T081241Z.0309348472c8719d.0efdbc7ba1c507292080e3fbffe4427f7ce9a9f0'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def upload_it(file):
  y = yadisk.YaDisk(token='AgAAAAAjOwEUAADLW_7eYegi80jllGHeChXwMJY')
  y.upload(file, f"/{file}")

def translate_it(from_file_path, to_file_path, from_lang, to_lang='ru'):
    """
    https://translate.yandex.net/api/v1.5/tr.json/translate ?
    key=<API-ключ>
     & text=<переводимый текст>
     & lang=<направление перевода>
     & [format=<формат текста>]
     & [options=<опции перевода>]
     & [callback=<имя callback-функции>]
    :param to_lang:
    :return:
    """
    with open(from_file_path, encoding='utf-8') as reader:
      string = reader.read()

    params = {
        'key': API_KEY,
        'text': string,
        'lang': f'{from_lang}-{to_lang}',
    }

    response = requests.get(URL, params=params)
    json_ = response.json()

    with open(to_file_path, 'w', encoding='utf-8') as writer:
      translate = ''.join(json_['text'])
      writer.write(translate)

# print(translate_it('В настоящее время доступна единственная опция — признак включения в ответ автоматически определенного языка переводимого текста. Этому соответствует значение 1 этого параметра.', 'no'))

if __name__ == '__main__':
  translate_it('DE.txt', 'DE_RU.txt', 'de')
  upload_it('DE_RU.txt')
  translate_it('ES.txt', 'ES_RU.txt', 'es')
  upload_it('ES_RU.txt')
  translate_it('FR.txt', 'FR_RU.txt', 'fr')
  upload_it('FR_RU.txt')

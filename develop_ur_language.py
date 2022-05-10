import random
from urllib import parse
from requests_html import HTMLSession

session = HTMLSession()

def check_in_dictionary_in_list (txt=""):
    parsed_text = parse.quote(txt)
    url = f"https://dictionary.cambridge.org/tr/s%C3%B6zl%C3%BCk/ingilizce-t%C3%BCrk%C3%A7e/{parsed_text}"
    res = session.get(url, headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"})
    return (res.html.find(".trans.dtrans.dtrans-se", first=True)).text
    
def translate(txt=""):
    parsed_text = parse.quote(txt)
    url = f"https://translate.google.com/m?sl=en&tl=tr&q={parsed_text}"
    res = session.get(url)
    data = res.html.find(".result-container", first = True).text
    return (data)

def get_word_list():
    url = f"https://www.ef.com/wwen/english-resources/english-vocabulary/top-3000-words/"
    res = session.get(url)
    return (str(res.html.find("p")[11].text)).split()

def run_app ():
    point = 0
    tp = 0
    fp = 0
    try:
        while True:
            word = random.choice(get_word_list())
            print (word)
            translated_word = translate(word)
            checked_word = str(check_in_dictionary_in_list(word))
            users_answer = input("Anlamı nedir? >>")
            cluster = set(())
            for checked_word_index in range(len(checked_word.split(","))):
                cluster.add(checked_word.lower().split(",")[checked_word_index])
            cluster.add(translated_word.lower())
            if users_answer.lower().strip(",") in translated_word.lower().split() or users_answer.lower().replace(" ","") in checked_word.replace(" ","").lower().split(","):
                print(f"****Doğru****\nDoğru cevaplar: {cluster}")
                point += 1
                tp += 1
            else:
                print(f"****Yanlış****\nDoğru cevaplar: {cluster}")
                point -= 1
                fp +=1
            print (f"Puan: {point}\n")
    except KeyboardInterrupt:
        print(f"Doğru sayınız: {tp}, Yanlış sayınız: {fp}")
    except:
        pass

run_app()
import requests
from concurrent.futures import ThreadPoolExecutor

class TextComparer():
    def __init__(self, url_list):
        self.url_list = url_list
        
    def download(self, url, filename):
        fname = 'modules/data_files/' + filename
        r = requests.get(url)
        if r.status_code != 200:
            raise NotFoundException('Fejl')
        else:
            with open (fname, 'wb') as fd:
                for chunk in r.iter_content(chunk_size=1024):
                    fd.write(chunk)
                print("Url downloaded")


    def multi_download(self):
        with ThreadPoolExecutor(5) as ex:
             for key in self.url_list:
                ex.submit(self.download, key, self.url_list[key])

    def __iter__(self):
        return self
    
    def urllist_generator():
        for url in self.url_list.keys():
            yield url

    def avg_vowels(self, text):
        count = 0
        sum = 0
        vowels = ["a", "e", "i", "o", "u", "u"]
        with open(text) as fd:
            for line in fd:
                for word in line.split():
                    w = word.lower()
                    for char in word:
                        if char in vowels:
                            sum += 1
                    count += 1
        return sum/count



    ##def hardest_read():
    

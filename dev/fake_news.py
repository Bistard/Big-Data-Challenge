from htmldate import find_date
from concurrent.futures import ThreadPoolExecutor 
from operator import itemgetter
import csv

files = ["fake_news/NewsFakeCOVID1.csv",
         "fake_news/NewsFakeCOVID2.csv",
         "fake_news/NewsFakeCOVID3.csv",
         "fake_news/NewsFakeCOVID4.csv"]
main_container = []
for path in files:
    with open(path, encoding="utf8") as file:
        lines = file.readlines()
        lines = [x.split(',') for x in lines] 
        urls = [[[int(x[0]), y] for y in x if str(y).startswith('http')] for x in lines ]
   
        [[main_container.append(y) for y in (x)] for x in urls]
 
    
data = []

def dateprinter(url): 
    try:
        required_data = find_date(url[-1])
        data.append([url[0],str(required_data)])
        print(url[0],required_data)
    except:pass    

def main():
    print(len(main_container))
    with ThreadPoolExecutor(max_workers=100) as executor:
        try:
            executor.map(dateprinter , main_container)
            executor.shutdown(wait=True)
        except:
            pass

if __name__ == '__main__':
    main()
    header = ['key','password']

    data = sorted(data, key=itemgetter(0))
    with open('output.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)
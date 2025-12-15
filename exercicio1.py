import requests

word = input("Search rhymes: ")
search_url = "https://api.datamuse.com/words?rel_rhy="
r = requests.get(search_url + word)
data = r.json()
if not data:
    print("No rhymes found.")
else:
    number_of_rhymes = len(data)
    print(str(number_of_rhymes) + " rhymes with " + word + ":")
    rhymes = sorted([item["word"] for item in data], key=len)
    for word in rhymes:
        print(word)

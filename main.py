def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)
    create_Report(book_path,get_word_count(text),get_character_count(text))
    #print(f"{get_word_count(text)} words found in the document")
    #print(f"{get_character_count(text)} characters found in the document")

def get_character_count(words):
    book_dict = {}
    book_path = "books/frankenstein.txt"
    for c in words:
        c = c.lower()
        if c in book_dict:
            book_dict[c] += 1
        else:
            book_dict[c]=1
    return book_dict


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(words):
    return len(words.split())

def sort_on(dict):
    return dict["count"]

def create_Report(bookPath, wordCount, charDict):
    alphabeticCharacters = []
    print(f"--- Begin report of {bookPath} ---")
    print(f"{wordCount} words found in the document")
    print()
    for element in charDict:
        if element.isalpha():
            alphabeticCharacters.append({"character": element, "count":charDict[element]})
    
    alphabeticCharacters.sort(reverse=True, key=sort_on)
    for element in alphabeticCharacters:
        print(f'The "{element["character"]}" character was found {element["count"]} times')




main()

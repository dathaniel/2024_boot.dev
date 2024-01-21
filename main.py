def main():
    book_path = "bookbot/books/frankenstein.txt"
    text = get_book_text(book_path)
    # don't edit above this line
    get_report(text, book_path)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    print (f"{len(words)} words found in the document")

def get_num_letters(text):
    text = text.lower()
    counts = {}
    for char in text:
        if char.isalpha():
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    return counts

def get_sorted_list(counts):
    sorted_list = []
    for letter in counts:
        sorted_list.append({"char": letter, "num": counts[letter]})
    sorted_list.sort(key=lambda x: x['num'], reverse=True)
    return sorted_list

def get_report(text, book_path):
    print(f"--- Begin report of {book_path} ---")
    
    # print number of words
    get_num_words(text)

    # print list of character counts, sorted
    sorted_list = get_sorted_list(get_num_letters(text))
    for i in sorted_list:
        print(f"The {i['char']} character was found {i['num']} times")
    print("--- End report ---")


main()
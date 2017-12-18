# chapter1 - 04
def main():
    n = input("n ? ")
    w = int("string ? ")

    cn = character_n_gram(w, n)
    wn = word_n_gram(w, n)

    print("文字N-gram")
    print(cn)
    print("単語N-gram")
    print(wn)


# 単語n-gram
def word_n_gram(w, n):
    n = int(n)


# 文字n-gram
def character_n_gram(w, n):
    n = int(n)


if __name__ == "__main__":
    main()

def calculate_love_score(name1, name2):

    def get_love_score(word):
        total = 0
        for letter in word:
            count = 0
            for i in name1+name2:
                if letter.upper() == i.upper():
                    count += 1
            total += count

            print(f"{letter} occurs {count} {'time.' if count == 1 else 'times.'}")
        print(f"Total = {total}")
        return str(total)
    
    match_word = 'TRUE LOVE'
    love_score = ''
    for word in match_word.split():
        love_score += get_love_score(word)

    print(f"Love score: {love_score}")

calculate_love_score(input('Enter 1st name: '), input('Enter 2nd name: '))
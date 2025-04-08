def calculate_love_score(name1, name2):
    
    def get_love_score(word):
        
        total = 0
        for letter in word:
            count = 0
            for i in name1+name2:
                if letter.upper() == i.upper():
                    count += 1
            total += count

            print(f"{letter} occurs {count} {'time' if count == 1 else 'times'}.")
        
        return str(total)
    
    love_score = ''
    match_str = 'TRUE LOVE'
    for word in match_str.split():
        #print(word)
        love_score += get_love_score(word)
    
    print(love_score)
        
#calculate_love_score("Kanye West", "Kim Kardashian")
calculate_love_score(input("Enter 1st name: "), input("Enter 2nd name: "))
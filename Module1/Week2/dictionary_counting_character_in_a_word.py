
character_statistic = {}
word = input("Nhap vao mot tu: ")
temp_word = word.lower()
for char in temp_word:
  if char in character_statistic:
    character_statistic[char] += 1
  else:
    character_statistic[char] = 1
print(character_statistic)  

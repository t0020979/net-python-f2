words = ['python', 'c++', 'c', 'scala', 'java'] 
letter = 'c'

def count_letter(words, letter):
  total = 0
  for word in words:
    if letter in word:
      total += 1
  return total

total = count_letter(words, letter)
print(f'Total words:{total} with letter {letter}')

with open("D:\Hoc Tap\KHOA HOC AIO 2024\AIO2024-Excercise\Module1\Week2\P1_data.txt", "r") as f:
  document_lines = f.read()

def processes_text(sentences):
  sentences = sentences.lower()
  sentences = sentences.replace(".", "").replace(",", "")
  sentences = sentences.split()
  return sentences
words = processes_text(document_lines)
def count_words_in_list(words):
  counter = {}
  for word in words:
    if word in counter:
      counter[word] += 1
    else:
      counter[word] = 1
  return counter
counter = count_words_in_list(words)
print(words)
print(counter)
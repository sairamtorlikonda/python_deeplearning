import csv
from collections import Counter

dna_dict = {}
with open(r"C:\Users\Sai Ram Torlikonda\Desktop\part-1\icp3\codon.tsv") as tsvfile:
  reader = csv.reader(tsvfile, delimiter='\t')
  for row in reader:
    try:
      dna_dict[row[0]] = row[1]
    except:
      pass
while True:
  dna_seq = input(" enter The input sequence: ")
  if len(dna_seq)%3 != 0 :
    print("DNA sequence not valid. Give a valid one")
    continue

  codons = [dna_seq[i:i+3] for i in range(0, len(dna_seq), 3)]
  print("The individual codon sequence is: ", codons)
  try:
    codon_names = list(map(lambda x: dna_dict[x], codons))
    break
  except:
    print("there is a codon sequence that doesn't lie in tsv file. Please give one other sequence")

name_counts = Counter(codon_names)
print("The names and count of codons: ", name_counts)
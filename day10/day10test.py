with open("Downloads/第十天附加材料/codon.txt","r")as file:
    dict={}
    num=0
    for line in file:
        num+=1
        if num==1:
            continue
        line.strip().split()
        codon=line[0]
        amino=line[1]
        dict[codon]=amino
        if amino=="stop":
            break
def transcript(DNA):
    trans={'A': 'U', 'T' :'A', 'C': 'G', 'G': 'C'}
    mRNA=''
    for num in DNA:
        mRNA.append(trans[num])
    return mRNA
def translate(DNA):
    amino_s=''
    mrna=transcript(DNA)
    start_index=mrna.find("AUG")
    i=start_index
    while i<len(mrna):
        codon_temp=mrna[i:i+3]
        amino_temp=dict[codon_temp]
        if amino_temp=="STOP":
            break
        amino_s+=amino_temp
        i+=3
    return amino_s
with open("Downloads/第十天附加材料/seq.fa","r")as file:
    current_name=""
    current=""
    seq_dict={}
    for lines in file:
        line=lines.strip()
        if line.startswith(">"):
            current_name=line[1:]
        else:
            current+=line
            seq_dict[current_name]=current
protein_dict={}
for name,sequence in seq_dict.items():
    protein_dict[name]=translate(sequence)
   
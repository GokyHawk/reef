from Bio import SeqIO
for seq_record in SeqIO.parse("16S_rRNA_sequence.fasta", "fasta"):
        print(seq_record.id)
        print(repr(seq_record.seq))
        print(len(seq_record))


def validate_sequence(seq, subseq):
    seq_id = 0
    subseq_id = 0
    while seq_id < len(seq) and subseq_id < len(subseq): 
        if seq[seq_id] == subseq[subseq_id]:
            subseq_id += 1
        seq_id += 1

    return subseq_id == len(subseq)

def validate_sequence_for(seq, subseq): 
    subseq_id = 0
    for value in seq: 
        if subseq_id == len(subseq):
            return True
        if value == subseq[subseq_id]:
            subseq_id += 1
    
    return subseq_id == len(subseq)
            

# Test cases
seq = [1, 2, 3, 4, 5, 6, 7]
subseq = [2, 3, 8]

isSubseq = validate_sequence_for(seq, subseq)

if isSubseq:
    print(f"Found the subsequence !!!\n")
else: 
    print("Didn't find the subsequence !!!")

def lavenschtein_distance(str1, str2): 
    edits = [[x for x in range(len(str1)+1)] for y in range(len(str2)+1)]
    for i in range(1, len(str2) + 1): 
        edits[i][0] = edits[i-1][0] + 1
    for r in range(1, len(str2) + 1): 
        for c in range(1, len(str1) + 1): 
            if str2[r-1] == str1[c-1]:
                edits[r][c] = edits[r-1][c-1]
            else: 
                edits[r][c] = 1 + min(edits[r-1][c], edits[r][c-1], edits[r-1][c-1])
    
    def print_2d_array(array):
        for row in array:
            print(row)

    print_2d_array(edits)
    return edits[-1][-1]

min_edits = lavenschtein_distance('yabd', 'abc')
print(f"The minimum number of edits that should be performed is given by {min_edits}")

def convert(s: str, num_rows: int) -> str:
    rows = []
    
    for lists in range(num_rows):
        rows.append([])
    
    count = 0
    
    for letter in s:
        if count == 0:
            isDown = true
        elif count == num_rows - 1
            isDown = False
        row[count].append(letter)
        
        if isDown:
            count+= 1
        else:
            count -= 1
    
    
convert("", 3)
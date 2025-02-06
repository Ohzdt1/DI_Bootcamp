#used external tools for this as I did not manage by myself 

matrix = [
    ['7', 'i', 'i'],
    ['T', 's', 'x'],
    ['h', '%', '?'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['^', 'r', '!']
]


def decode_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    decoded_text = ""
    temp_text = ""

    for col in range(cols):
        for row in range(rows):
            char = matrix[row][col]
            if char.isalpha():  
                temp_text += char
            else:  
                temp_text += " "

    decoded_text = ' '.join(temp_text.split())

    return decoded_text

message = decode_matrix(matrix)
print("Decoded Message:", message)

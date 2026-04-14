cat <<EOF > 0-square_matrix_simple.py
#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_matrix.append([x**2 for x in row])
    return new_matrix    
EOF    

print(f"PART 1")
print(f" ")

#2a."x = 1.825" yields an error message: 'float' because the object cannot be interpreted as an integer
x = 18

#1a. binary and hex forms of a variable
print(x, bin(x), hex(x))

#3a. you can assign hex and binary values to a variable
y = 0b1011
z = 0xA3
print(y, z)

#4a. we can add numbers of any representation
w = x + y + z
print(f"the sum is: ", w)

print(f" ")
print(f"COMPRESSION")
print(f" ")

print(f"Enter original size: ")
original_size = input()

print(f"Enter dictionary size: ")
dictionary_size = input()

print(f"Enter compressed text size: ")
compressed_txt_size = input()

#1b. display user inputs
print(f" ")
print(f"Original size: ", original_size, f" characters")
print(f"Dictionary size: ", dictionary_size, f" characters")
print(f"Compressed text size: ", compressed_txt_size, f" characters")

#convert inputs to integers
original_size = int(original_size)
dictionary_size = int(dictionary_size)
compressed_txt_size = int(compressed_txt_size)

#Variable A simplifies the math within the compression formula
A = compressed_txt_size + dictionary_size
print(f"Total: ", A, f" characters")

#2b. Compression formula
compression_percent = ((original_size - A) / original_size) * 100

#Uses round() function to round 2 decimal places for percentage
compression_percent = round(compression_percent, 2)

#prints result
print(f"Compression:  ", compression_percent, f"%")

# this is dirty code to make useless but funny things

text = input("texte: ")

hex_ = bytes(text, "UTF-8").hex()

final_str = ""
for loop in range(1):
    # encode
    final_str = ""
    actual_hex = ""
    for i in range(len(hex_)):
        actual_hex += hex_[i]
        if len(actual_hex) == 4:
            char = chr(int(actual_hex, base=16))
            final_str += char
            actual_hex = ""

    if actual_hex != "":
        char = chr(int(actual_hex, base=16))
        final_str += char

    hex_ = bytes(final_str, "UTF-8").hex()

    # print(len(text))
    # print(len(final_str))
    # print(final_str)

print(final_str)

input_decode = final_str
output = ""
for loop in range(1):
    # decode
    for char in input_decode:
        ord_hex = hex(ord(char))[2:]
        output += ord_hex
    input_decode = bytes.fromhex(output).decode("UTF-8")
    output = ""

print(input_decode)
# print(bytes.fromhex(input_decode).decode("UTF-8"))

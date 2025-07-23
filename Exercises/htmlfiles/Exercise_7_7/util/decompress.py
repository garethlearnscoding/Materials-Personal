import csv

def read_compress(file_name,folder):
    print("Function: read_compress")
    file_path = f"./{folder}/{file_name}"
    with open(file_path, mode='r') as file:
        data = file.read()
    return data


def decompress_data(data_set):
    print("Function: decompress_data")
    byte = ""
    decompressed_data = []
    try:
        for i in data_set:
            if int(i) in [0,1] and len(byte) < 3:
                byte += i
            elif int(i) in [0,1] and len(byte) == 3:
                # print(f"Byte: {Byte}")
                decompressed_data.append(byte)
                byte = i
            else:
                # print(f"Byte: {byte}")
                # print(f"Multiply: {i}")
                decompressed_data += [byte] * int(i)
                byte = ""
                # print(f"Decompressed Data: {decompressed_data}")
        decompressed_data = [[i] for i in decompressed_data]
        return decompressed_data
    except ValueError:
        return False

def write_decompress(decompressed_data,folder):
    print("Function: write_decompress")
    if not decompressed_data:
        return True
    else:
        file_name = "decompressedimage.txt"
        file_path = f"./{folder}/{file_name}"
        with open(file_path,"w",newline="\n") as store:
            writer = csv.writer(store)
            writer.writerows(decompressed_data)




if __name__ == "__main__":
    data_set = read_file("compressedimage.txt")
    decompressed_data = decompress_data(data_set)
    print(decompressed_data)
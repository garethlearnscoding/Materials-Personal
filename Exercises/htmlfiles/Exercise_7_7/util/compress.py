import csv

def read_decompress(file_name,folder):
    print("Function: read_decompress")
    file_path = f"./{folder}/{file_name}"
    with open(file_path, mode='r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data

def compress_data(data_set):
    print("Function: compress_Data")
    grid_w,grid_l = 9,9
    compress_data_string = ""
    checker = 0
    first_row = True
    if len(data_set) != grid_l*grid_w:
        return False
    for i in data_set:
        if checker == grid_w or first_row:
            temp = i[0]
            compress_data_string += temp
            count = 1
            first_row = False
            checker = 1
        else:
            checker += 1
            if i[0] != temp:
                if count == 1:
                    count = ""
                compress_data_string += str(count)
                temp = i[0]
                compress_data_string += str(temp)
                count = 1
            else:
                count +=1
            
    return compress_data_string

def write_compress(data,folder):
    if not data:
        return True
    else:
        print("Function: write_compress")
        file_name = "compressedimage.txt"
        file_path = f"./{folder}/{file_name}"
        with open(file_path, "w") as store:
            store.write(data)
        

if __name__ == "__main__":
    data = read_file("imagefile.txt")
    compressed_data_string = compress_data(data)
    store_data(compressed_data_string)



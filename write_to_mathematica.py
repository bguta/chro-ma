
def write(data):
    data_str = str(data).replace("[","{").replace("]","}")
    with open("data.txt","w") as f:
        f.write(data_str)

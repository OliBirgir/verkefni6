def read_filename():
    name = input("Input a file name:")
    return name

def year():
    year = input("Enter a Year: ")
    return year

def open_file(filename):
    try:
        file_object = open(filename,"r")
        return file_object
    except:
        print("Filename",filename,"not found!")

def sort_file(file_open):
    listoftxt = []
    for lines in file_open:
        listoftxt.append(lines.strip().split())
        #listoftxt.append.split(',')
    print(listoftxt)
        









#main
filename = read_filename()
year = year()
file_open = open_file(filename)
sorter = sort_file(file_open)




#finna filename
#finna year
#opna skrá
#
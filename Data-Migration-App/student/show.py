

# L = [ [101,'AAA', 60],[102,'BBB', 70],[103,'CCC',80] ]

def display_student_information(list_of_list): # L is list of List
    print("RNO \t NAME \t PER")
    for record in list_of_list:
        print(record[0], "\t", record[1], "\t",record[2])
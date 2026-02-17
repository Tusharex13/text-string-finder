print("<<<This program is case sensitive!>>>")


    ##file operation


filename = input("Enter file name: ")
try:
    with open(filename, encoding="utf-8") as loaded_file:
        read_file = loaded_file.read()
except FileNotFoundError:
    print("File not found!")
    exit()
    
    ###variables###
#line_location = []
#line_and_count_loc = []
#page_ver_after = []
locations = []
occurrence = 0
line_numbers = []
current_line = 1
last_pos = 0
    #take input for what to search and where to go
user_search = input(f"Type what you are looking for.\n")
if user_search == "":
    print("Empty search not allowed.")
    exit()

    #find the user input in the file for the first time
temp_location = read_file.find(user_search)#kj

    ##what if we don't find or find?

while temp_location != -1:

    occurrence += 1
    locations.append(str(temp_location))
    #current_line = read_file.count("\n", 0, temp_location) + 1

    newlines_since_last = read_file.count("\n", last_pos, temp_location)
    current_line += newlines_since_last

    last_pos = temp_location + 1
    line_numbers.append(str(current_line))
    
    temp_location = read_file.find(user_search, last_pos)
    #line_and_count_loc.append(str(temp_location))

print("Count:", occurrence,'\n')
#print("Locations:", locations,'\n')
print("Lines:", line_numbers,'\n')

flag = 0
if occurrence > 0:
    input_f_line = input(f"On which number of 'count' do you wanna go?\nIf not type 'quit' or 'exit' or 0.\n")
    user_line = input_f_line.lower()
    
    sp_line = 0
    if input_f_line == "exit" or input_f_line == "quit" or input_f_line == "0":
        print("<<<exit>>>")
        flag = -1

    elif input_f_line.isdigit() and int(input_f_line) <= occurrence:
        input_f_line = int(input_f_line)
        flag = 1

    else:
        print("Invalid input!")

if flag == 1:
    try:
        special_line = int(line_numbers[input_f_line - 1]) - 1

        foreline = 0
        sh = int(locations[input_f_line-1])
        k = special_line - 50
        found_at = 0
        if k < 0:
            k = 0

        for i in range(k):
            #foreline = read_file[foreline:].find("\n")
            found_at = read_file.find("\n", foreline)
            foreline = found_at + 1


        totaline = read_file.count("\n") + 1
        k = k + 101
        if k > totaline:
            k = totaline
        found_at_2 = 0
        foreline_1 = foreline
        for ji in range(101):
            found_at_2 = read_file.find("\n", foreline_1)

            # --- THE EMERGENCY BRAKE ---
            if found_at_2 == -1:
                foreline_1 = len(read_file) # Point to the very end of the text
                break # Stop looping immediately
            foreline_1 = found_at_2 + 1

        page_content = read_file[foreline:foreline_1]
        HIGHLIGHT = "\033[1;30;43m" 
        RESET = "\033[0m"
        print("\n" + "="*100)
        print(page_content.replace(user_search, f"{HIGHLIGHT}{user_search}{RESET}"))
        print("=" * 100 + "\n")
    except Exception as e:
        print(f"Error: {e}")


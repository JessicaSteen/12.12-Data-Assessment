log_file = open("um-server-01.txt")


def sales_reports(log_file):   #creating a function called sales_report, with a paramater of log_file
    for line in log_file:   # looping through each line in log_file
        line = line.rstrip() #removing the whitespace from the line it grabs and assigning value to new variable
        day = line[0:3]   #grabbing value from the line starting at index 0, grabbing 3 and assigning it to a new variable
        if day == "Mon": # the the day they grab is equal to Tuesday 
            print(line)  #print the line


sales_reports(log_file)

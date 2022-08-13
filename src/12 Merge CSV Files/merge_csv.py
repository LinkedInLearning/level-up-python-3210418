import csv

def merge_csv(csv_list, output_path):
    # build list with all fieldnames
    fieldnames = list()
    for file in csv_list:
        with open(file, 'r') as input_csv:
            fn = csv.DictReader(input_csv).fieldnames
            fieldnames.extend(x for x in fn if x not in fieldnames)

    # write data to output file based on field names
    with open(output_path, 'w', newline='') as output_csv:
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        writer.writeheader()
        for file in csv_list:
            with open(file, 'r') as input_csv:
                reader = csv.DictReader(input_csv)
                for row in reader:
                    writer.writerow(row)

# commands used in solution video for reference
if __name__ == '__main__':
    merge_csv(['class1.csv', 'class2.csv'], 'all_students.csv')

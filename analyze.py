import collections
import csv

def main():
    agency_counter = collections.Counter()
    complaint_counter = collections.Counter()
    with open('data.csv') as fp:
        reader = csv.DictReader(fp)
        for line in reader: 
            agency = line.get('Agency Name')
            agency_counter[agency] += 1
            complaint = line.get('Complaint Type')
            complaint_counter[complaint] += 1

    for complaint, count in complaint_counter.most_common():
        print(complaint, count)


main()    

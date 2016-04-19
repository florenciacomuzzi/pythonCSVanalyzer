import collections
import csv

def main():
    agency_counter = collections.Counter()
    with open('data.csv') as fp:
        reader = csv.DictReader(fp)
        for line in reader: 
            agency = line.get('Agency Name')
            agency_counter[agency] += 1

    for agency, count in agency_counter.most_common():
        print(agency, count)


main()    

import collections
import csv

def main():
    agency_counter = collections.Counter()
    complaint_counter = collections.Counter()
    with open('data.csv') as fp:
        reader = csv.DictReader(fp)
        noise_counter = 0
        total = 0
        for line in reader:
            total += 1 
            agency = line.get('Agency Name')
            agency_counter[agency] += 1
            complaint = line.get('Complaint Type')
            complaint_counter[complaint] += 1

    
    for complaint, count in complaint_counter.most_common():
        if 'noise' in complaint.lower():
            noise_counter += 1
        complaint_counter[complaint] += 1
       
    for complaint, count in complaint_counter.most_common():
        print(complaint, count)
    print()
    print('Noise Complaints: ', noise_counter)
    print('Noise %', (noise_counter / total) * 100)

main()    

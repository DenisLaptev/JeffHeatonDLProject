import csv
import urllib.request
import codecs
import numpy as np

'''
Pandas will read the entire CSV file into memory. 
Usually, this is fine. However, at times you may wish to "stream" a very large file. 
This allows you to process this file one record at a time. 
Because the file is not loaded into memory, 
you are able to process extremely large files. 
The following code loads the Iris dataset and calculates averages, one row at a time. 
This would work for extremely large files.
'''


url = "https://data.heatonresearch.com/data/t81-558/iris.csv"
urlstream = urllib.request.urlopen(url)
csvfile = csv.reader(codecs.iterdecode(urlstream, 'utf-8'))
next(csvfile)  # Skip header row
sum = np.zeros(4)
count = 0

for line in csvfile:
    # Convert each row to Numpy array
    line2 = np.array(line)[0:4].astype(float)

    # If the line is of the right length (skip empty lines), then add
    if len(line2) == 4:
        sum += line2
        count += 1

# Calculate the average, and print the average of the 4 iris measurements (features)
print(sum / count)

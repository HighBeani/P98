lowerlimit = int(input('Enter the lower limit here (Integer)'))
upperlimit = int(input('Enter the upper limit here (Integer)'))
number = int(input('Enter the dividing number here (Integer)'))
while lowerlimit <= upperlimit:
    lowerlimit += 1
    if lowerlimit%number != 0:
        continue
    print(lowerlimit)
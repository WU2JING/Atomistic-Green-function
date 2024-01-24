data = open('data','r')
line = data.readline()
output_file0 = open('layer_map_file' + str(0), 'w')
output_file1 = open('layer_map_file' + str(1), 'w')
output_file2 = open('layer_map_file' + str(2), 'w')
output_file3 = open('layer_map_file' + str(3), 'w')
output_file4 = open('layer_map_file' + str(4), 'w')
output_file0.write('layer' + ' ' +  str(0) + ' ' + str(120) + '\n')
output_file1.write('layer' + ' ' +  str(1) + ' ' + str(120) + '\n')
output_file2.write('layer' + ' ' +  str(2) + ' ' + str(120) + '\n')
output_file3.write('layer' + ' ' +  str(3) + ' ' + str(120) + '\n')
output_file4.write('layer' + ' ' +  str(4) + ' ' + str(120) + '\n')

while line:
    tmp = float(line.split()[2])
    if  tmp < 8:
        output_file0.write(line.split()[0] + ' ' + line.split()[1] + '\n')
    elif 8 < tmp < 16:
        output_file1.write(line.split()[0] + ' ' + line.split()[1] + '\n')
    elif 16 < tmp < 23:
        output_file2.write(line.split()[0] + ' ' + line.split()[1] + '\n')
    elif 23 < tmp < 31:
        output_file3.write(line.split()[0] + ' ' + line.split()[1] + '\n')
    elif 31 < tmp :
        output_file4.write(line.split()[0] + ' ' + line.split()[1] + '\n')
    line = data.readline()
data.close()

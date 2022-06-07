def k(line):
    v = line.partition("risks%20")[2]
    v = v[0] if v else 'z' # here z stands for the max value
    return v
print ''.join(sorted(open('COPosterLinks.txt', 'rb'), key = k))

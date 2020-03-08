import csv

class Hashcode:
    def __init__(self):
        pass
    
    csv_row = list()
    libraries= []
    books = []
    
    def readLibraries(self):
        i=2
        while( i < len(csv_row)):
            lib = {'no_books': csv_row[i][0], 'signup':csv_row[i][1], 'ships':csv_row[i][2]}
            bs = csv_row[i+1]
            libraries.append(lib)
            books.append(books)
            i = i+2
            
    def computeStartTimes(self):
        startDay = 0
        print(libraries[0])
        for i in range(0, L):
            print(libraries[i]['signup'])
            startDay += libraries[i]['signup']
            libraries[i]['startTime'] = startDay
    
    def computeBooksPerLibrary(self):
        for i in range(0, L):
            startTime = libraries[i]['startTime']
            if S - startTime <= 0:
                libraries[i]['capacity'] = 0
            else:
                libraries[i]['capacity'] = min( (S - startTime ) * libraries[i]['ships'], libraries[i]['no _books'])
    
    def run(self):
        for line in open("a_example.txt"):
            csv_row.append( line.split())
        
        B = csv_row[0][0] #books
        L = csv_row[0][1] #libraries
        S = csv_row[0][2] #days for scanning
        
        score = csv_row[1]
        
        #library:
        #no_books
        #signup
        #ships
        #startTime
        #capacity
        self.readLibraries()
        self.computeStartTimes()
        self.computeBooksPerLibrary()
        
if __name__ == '__main__':
    x = Hashcode()
    x.constructor()
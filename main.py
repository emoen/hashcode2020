import csv

csv_row = list()
libraries= []
books = []
B = 0
L=0
S=0

my_score=0
    
def hashcode():
    csv_row = list()
    libraries= []
    books = []
    my_score=0
    for line in open("a_example.txt"):
        csv_row.append( line.split())
    
    for i in range(0,len(csv_row)):
        for j in range(0, len(csv_row[i])):
            csv_row[i][j]=int(csv_row[i][j])
    
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
    readLibraries()
    unique_books = set().union(*books)
    is_scanned = [0 for i in range(0, len(unique_books))]
    computeStartTimes()
    #computeBooksPerLibrary()
     
def readLibraries():
    i=2
    while( i < len(csv_row)):
        lib = {'no_books': csv_row[i][0], 'signup':csv_row[i][1], 'ships':csv_row[i][2], 'booksToScan':[]}
        lib_books= csv_row[i+1] 
        lib['books'] = lib_books
        libraries.append(lib)
        books.append(lib_books)
        i = i+2
    print(books)
            
def computeStartTimes():
    startDay = 0
    print(libraries[0])
    for i in range(0, L):
        startDay += libraries[i]['signup']
        libraries[i]['startTime'] = startDay
        print(libraries[i])
    
def computeBooksPerLibrary():
    for i in range(0, L):
        startTime = libraries[i]['startTime']
        if S - startTime <= 0:
            libraries[i]['capacity'] = 0
        else:
            libraries[i]['capacity'] = min( (S - startTime ) * libraries[i]['ships'], libraries[i]['no_books'])
    
def assignBooksToLibraries():
    global my_score
    for i in range(0,L):
        lib = libraries[i]
        j = 0
        k=0
        lib['booksToScan'] = []
        while j < lib['capacity'] and k < lib['no_books']:
            lib['books'][k]
            if is_scanned[lib['books'][k]] == 0:
                lib['booksToScan'].append(lib['books'][k])
                is_scanned[lib['books'][k]] = 1                
                my_score += score[lib['books'][k]]
                j+=1
            k+=1
            
def GenerateOutput():
    var ret =[]
    nLibsNonZero = nnz();
    ret.Add(new int[] { nLibsNonZero });
    for (int i = 0; i < L; i++)
    {
        var lib = libraries[libraryOrder[i]];
        if (lib.booksToScan.Count > 0)
        {
            ret.Add(new int[] { libraryOrder[i], lib.booksToScan.Count });
            ret.Add(lib.booksToScan.ToArray());
        }
    }
    return ret;
        }
        
if __name__ == '__main__':
    hashcode()
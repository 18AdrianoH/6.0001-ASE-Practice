'''
Encapsulator for various static sorting methods.
'''
class Sorter(object):

    '''
    Initialization of the object, though it's unlikely that anyone will use it since
    the methods are static.
    '''
    def __init__(self):
        pass
    '''
    All sorted methods are highly imperative changing the actual ls object.
    To get something that returns a sorted version of your ls please use the unique_sorted()
    function with your favorite sorting function.

    You can turn on the debug parameter/flag to tell the function that you want helpful print statements
    of time and processing to help understand how runtime and memory usage as well as execution are going.
    '''
    # TODO: ADD DIFFERENT COMPARISON FUNCTIONS

    '''
    The good 'ol quicksort.
    '''
    @staticmethod
    def quick_sort(ls,debug=False):
        def qs(lis,db=False):
            pass
        def par(lis,db=False):
            pass
        pass
    
    '''
    Merge sort helpers.
    '''
    @staticmethod
    def merge(ls1,ls2):
        #print ls1
        #print ls2
    	ls3 = []
        lss1 = ls1[:]
        lss2 = ls2[:]
        while len(lss1) > 0 and len(lss2) > 0:
            if lss1[0] > lss2[0]:
                ls3.append(lss2[0])
                lss2 = lss2[1:]
            else:
                ls3.append(lss1[0])
                lss1 = lss1[1:]
            pass
        if len(lss1) > 0:
            ls3.extend(lss1)
        elif len(lss2) > 0:
            ls3.extend(lss2)
        return ls3
    @staticmethod
    def sortp(lis):
        if len(lis) == 1:
            return lis
        else:
            left = lis[:len(lis)//2]
            right = lis[len(lis)//2:]
            return Sorter.merge(Sorter.sortp(left),Sorter.sortp(right))
    '''
    Divide and conquer version of selection sort that works in nlogn since
    for n items in a tree it must go up logn levels and do this for each item.
    '''
    @staticmethod
    def merge_sort(ls,debug=False):
        return Sorter.sortp(ls)
    
    '''
    Swap items if not in order... repeat until sorted.
    '''
    @staticmethod
    def bubble_sort(ls,debug=False):
        sorted = False
        lls = len(ls)
        while (not sorted):
            sorted = True
            for index in range(0,lls-1):
                if (ls[index+1]<ls[index]):
                    sorted = False
                    (ls[index], ls[index+1]) = (ls[index+1], ls[index])
                    pass
                pass
            pass
        pass
    
    '''
    Sort by inserting items where they belong... so like 9 8 3 4 -> 3 9 8 4 - > 3 4 9 8 - > 3 4 8 9
    '''
    @staticmethod
    def insertion_sort(ls,debug=False):
        for pointer in range(1,len(ls)):
            pointert = pointer
            while pointert > 0 and ls[pointert-1] > ls[pointert]:
                (ls[pointert-1],ls[pointert]) = (ls[pointert],ls[pointert-1])
                pointert = pointert - 1
                pass
            pass
        pass

    '''
    Sort by selecting the smallest item and putting it at the front.
    '''
    @staticmethod
    def selection_sort(ls,debug=False):
        lls = len(ls)
        for index in range(0,lls):
            min_index = index
            for mini in range(index+1,lls):
                if (ls[mini] < ls[min_index]):
                    min_index = mini
                    pass
                pass
            (ls[index], ls[min_index]) = (ls[min_index], ls[index])
            pass
        pass
    
    '''
    Heapify and sort that way.
    '''
    @staticmethod
    def heap_sort(ls):
        pass
    
    '''
    Sorted returns a sorted version of the function.
    You must pass your sort function from one of the above and your list
    (or your function must be identical in API to the ones above.)
    '''
    @staticmethod
    def unique_sorted(sort_function,ls,db=False):
        sorted_ls = ls[:] # Here you can also use = ls.copy()
        sort_function(ls,debug=db)
        return sorted_ls
    pass
##
##CMPS 2200  Recitation 1
##

### the only imports needed are here

import time

import tabulate

###


def linear_search(mylist, key):
  ##done. 
  for i, v in enumerate(mylist):
    if v == key:
      return i
  return -1


def binary_search(mylist, key):
  ##done. 
  return _binary_search(mylist, key, 0, len(mylist) - 1)


def _binary_search(mylist, key, left, right):
  
  ##Recursive implementation of binary search.

  ##Params:
   ## mylist....list to search
   ## key.......search key
   ## left......left index into list to search
   ## right.....right index into list to search
  
  ##index of key in mylist, or -1 if not present.

  ### TODO
  ##splits the list in half and checks if the key is in the left or right half of the 
  ##list
  ##if the key is less than the mid value the key searches the 
  ##left half of the list by recursively calling the function
  ##if the key is greater than the mid value the key searches the right half of       
  ##the list by recursively calling the function
  if right >= left:
    mid = (right + left) // 2
    ##base case if the mid value equals the key return mids index
    if mylist[mid] == key:
      return mid
    elif mylist[mid] > key:
      return _binary_search(mylist, key, left, mid - 1)
    else:
      return _binary_search(mylist, key, mid + 1, right)
  else:
    return -1


def time_search(search_fn, mylist, key):
  
##	Return the number of milliseconds to run this
## search function on this list.

  ##Note 1: `search_fn` parameter is a function.
  ##Note 2: time.time() returns the current time in seconds. 
  ##You'll have to multiple by 1000 to get milliseconds.

  ##Params:
  ##sort_fn.....the search function
  ##mylist......the list to search
  ##key.........the search key 

  ##Returns:
  ##the number of milliseconds it takes to run this
  ##v search function on this input.

  ### TODO
  ##Marks start time runs the function then marks end time, returns the ##difference 
##between start and end * 1000 to return time in miliseconds"""
  start = time.time()
  search_fn(mylist, key)
  end = time.time()
  return int((end - start) * 1000)


def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
  ###
  ##Compare the running time of linear_search and binary_search
  ##for input sizes as given. The key for each search should be
  ##-1. The list to search for each size contains the numbers from 0 to n-1,
  ##sorted in ascending order. 

  ##You'll use the time_search function to time each call.

  ##Returns:
    ##A list of tuples of the form
##(n, linear_search_time, binary_search_time)
##indicating the number of milliseconds it takes
##for each method to run on each value of n
  ###
  ###Creates a list to store the tuples of the form then calculates the time using 
##time_search and adds to linear/binary_time then adds the tuples to the list 
##results
  results = []
  for n in sizes:
    mylist = list(range(int(n)))
    linear_time = time_search(linear_search, mylist, -1)
    binary_time = time_search(binary_search, mylist, -1)
    results.append((int(n), linear_time, binary_time))
  return results


def print_results(results):
  ##done 
  print(
      tabulate.tabulate(results,
                        headers=['n', 'linear', 'binary'],
                        floatfmt=".3f",
                        tablefmt="github"))



print_results(compare_search())

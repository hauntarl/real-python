'''
What "sorting" means in programming?
. putting a collection of elements in a well-defined order
. this implies that there must be a way to compare elements in that collection
. often this can be a simple numerical comparison or something lot more complex 
. imagine you have a database with information abour customers at an online 
  store, and you're trying to determine who to invite to participate in rewards
  program
. you might want to give priority to people who have been customers longest but 
  also want to weigh how much money each customer has spent and when was the 
  last time they made a purchase

Keywords
. Runtime: how quickly the algorithms runs (O(n), O(n log(n)), O(n^2), etc.)
. Stable sort: an algorithm that generates stable results when sorted multiple
  times (eg. if you sort a list of store items alphabetically, then by price, 
  are the items that are equal in price still sorted alphabetically?)
. In-place sort: an algorithm that doesn't require any additional memory space
  other than the memory taken up by its input
. Pathological case: A case in which the input data is specifically designed to 
  make your algorithm run as slowly as possible

Why Sorting Matters?
. Searching: for an item on a list works much faster if the list is sorted
. Selection: selecting items from a list based on their relationship to the rest
  of the items is easier with sorted data. eg. finding kth largest or smallest,
  finding the median value of the list, etc.
. Duplicates: Finding duplicate values on a list can be done very quickly
. Distribution: Analyzing the frequency distribution of items on a list is very
  fast if the list is sorted. eg. finding the element that appears most or least

Time Complexity
. two general ways to measure how long an algorithm takes
  - directly   (in mins, secs, millisecs, etc.)
  - indirectly (in terms of no. of operations completed)
. Big-O notation: represents a worst case runtime of an algorithm as a function
  of no. of operations compared to the size of the input, or n.
. algorithms can be divided into classes based on their worst-case runtime.
  c > log(n) > n > n log(n) > n^2 > c^n > n!
. certain algorithms in the same classes might be faster or slower than one 
  another in practice, but this is an easy way to classify runtimes generally
'''

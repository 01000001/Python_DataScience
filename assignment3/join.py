import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(input_all):

    mr.emit_intermediate(input_all[1], input_all)

def reducer(key, list_of_values):
    # key: word
    # value: name of the book

    output_all = []

    for item in list_of_values[1:]:
        # fill up total with the list of values items
        total = list_of_values[0] + item

        mr.emit((total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

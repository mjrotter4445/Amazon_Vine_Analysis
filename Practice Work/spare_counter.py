##pip3 install MRJob
#from mrjob.job import MRJob
 
from mrjob.job import MRJob
class spare_count(MRJob):
   def mapper(self, _, line):
       for word in line.split():
           if word.lower() == "spare":
               yield "spare", 1

   def reducer(self, key, values):
       yield key, sum(values)
if __name__ == "__main__":
   spare_count.run()
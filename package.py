import knapsack
from __future__ import print_function
import pyslurm
import sys
from time import gmtime, strftime

#Sample Jobs
windowsize = 5
jobsize = [3, 1, 5, 4]
pweight = [60, 50, 30, 40]
capacity = 230


def solveKnapsack():
	global jobsize
	global pweight
	global capacity
	for i in range(len(jobsize)):
		powerweight.append(jobsize[i] * pweight[i])
	
	return knapsack.knapsack(jobsize, powerweight).solve(capacity)


def main(power_capacity, num_nodes_capacity):

	if (len(sys.argv) == 2):
		global capacity
		capacity = int(sys.argv[1])

		
	try:
		a = pyslurm.job()
		myjobs = a.get()
		jobs = myjobs[0:windowsize]
		job_size = len(jobs)
		
		if (job_size > 0):
			print "JobIDs - %s" % a.ids() #JobIDs - [6, 7, 8, 9] 
			print "JobIDs in Running state - %s" % a.find('job_state', 'Running')
			#display(jobs)
			#njobs = len(jobs)
			#pending = a.find('job_state', 'PENDING')
		else:
			print("No jobs found !")

	except ValueError as e:
		print("Job query failed - {0}".format(e.args[0]))

	answer = solveKnapsack()
	print(answer)

if __name__ == "__main__":
	main()
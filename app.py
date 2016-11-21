#Written by Shreyas Moudgalya
#!/usr/bin/env python

from __future__ import print_function

import pyslurm
import sys
from time import gmtime, strftime

"""
if(col < wt[row]) then T[row][col] = T[row-1][col]
else T[row][col] = max(val[row] + t[row-1][col - wt[row]], t[row-1][col])
"""

def main(power_capacity, num_nodes_capacity):
	try:
		a = pyslurm.job()
		jobs = a.get()
		job_size = len(jobs)
		table = [power_capacity+1][job_size]
		if (job_size > 0):
			display(jobs)
			njobs = len(jobs)
			pending = a.find('job_state', 'PENDING')
		else:
			print("No jobs found !")

	except ValueError as e:
		print("Job query failed - {0}".format(e.args[0]))
	

def displayJobDict(job_dict):
    if job_dict:
        for key, value in sorted(job_dict.iteritems()):
            print("JobID {0} :".format(key))


def solve(a, power_capacity,job_size):
    #Initialize the entire table to -1
    for i in range(power_capacity+1):
        table.append([])
        for j in range(job_size):
            table[i].append(-1)

    getCell(power_capacity, job_size-1)
    best = traceTable();

    if (power_capacity != -1):
            #best.setApproach("Dynamic programming with power capacity found")
    else:
            #best.setApproach("Dynamic programming found")

    return best;

	
	
	
def getCell(row, col):
    if (col < 0 || row < 0):
        return 0

    item = jobs[col]

    within=None
    without=None
    cell = table[row][col]

        #If not memoized
        if (cell == -1):
            if (item.getTotalPowerForRacks() > row): #Change
                within = -1
            else:
                within = item.getNumRacks() + getCell(row - (int)item.getTotalPowerForRacks(), i - 1) #Change


            without = getCell(row, col-1);

            #Check to make sure we're within the value limit.
            if (within > num_nodes_capacity):
                within = 99999 #Fix

            cell = max(within, without)
            #memoized
            table[row][col] = cell

    return cell


	
def JobQueue():
	a = pyslurm.job()
	jobs = pyslurm.get()
	
	if jobs:
		date_fields = [ 'start_time','suspend_time','submit_time','end_time','eligible_time','resize_time']

		for key, value in jobs.iteritems():
			print "Job ID : %s" % (key)
			for part_key in sorted(value.iterkeys()):
				if part_key in date_fields:
					if value[part_key] == 0:
						print "\t%-20s : N/A" % (part_key)
					else:
						ddate = gmtime(value[part_key])
						ddate = strftime("%a %b %d %H:%M:%S %Y", ddate)
						print "\t%-20s : %s" % (part_key, ddate)
				else:
					print "\t%-20s : %s" % (part_key, value[part_key])
			print "-" * 80
	else:
		print "No jobs found !"
	
	
def traceTable(power_capacity, jobs):
	best = []
	row = power_capacity
	col = jobs.size() - 1
	
	while (col >= 0):
		item = jobs[col]
		without = col == 0 ? 0 : table[row][col - 1]
		if(table[row][col] != without):
			best += item
			row -= round(item.getTotalPowerForRacks())
		col -= 1
	return best


def printResultTable(jobs, num_nodes_capacity, table):
	print("\n")
	job_size = len(jobs)

	for r in range(num_nodes_capacity+1):
		for c in range(job_size):
			print(table[r][c] + "\t")
		print("\n")

	
if __name__ == "__main__":
	#num_nodes_capacity
	#power_capacity
	main()

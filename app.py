#!/usr/bin/env python

from __future__ import print_function

import pyslurm
import sys

table = []


@Override
def display(job_dict):
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




def getCell(j, i):
    if (i < 0 || j < 0):
        return 0

    item = jobs[i]

    within=None
    without=None
    cell = table[j][i]

        #If not memoized
        if (cell == -1):
            if (item.getTotalPowerForRacks() > j): #Change
                within = -1
            else:
                within = item.getNumRacks() + getCell(j - (int)item.getTotalPowerForRacks(), i - 1) #Change


            without = getCell(j, i - 1);

            #Check to make sure we're within the value limit.
            if (within > num_nodes_capacity):
                within = 99999 #Fix

            cell = max(within, without)
            #memoized
            table[j][i] = cell

    return cell


def traceTable():
    pass




if __name__ == "__main__":

    try:
        a = pyslurm.job()
        jobs = a.get()
        job_size = len(jobs)
        if job_size > 0:

            display(jobs)
			njobs = len(jobs)

            pending = a.find('job_state', 'PENDING')
        else:
            print("No jobs found !")
    except ValueError as e:
print("Job query failed - {0}".format(e.args[0]))

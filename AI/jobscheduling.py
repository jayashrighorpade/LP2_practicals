def job_scheduling(jobs):
    # Sort jobs based on their deadlines in ascending order
    sorted_jobs = sorted(jobs, key=lambda x: x['deadline'])

    schedule = []
    current_time = 0

    for job in sorted_jobs:
        processing_time = job['processing_time']
        deadline = job['deadline']

        # Check if the job can be scheduled within its deadline
        if current_time + processing_time <= deadline:
            schedule.append(job)
            current_time += processing_time

    return schedule

# Example jobs
jobs = [
    {'id': 'Job 1', 'processing_time': 2, 'deadline': 5},
    {'id': 'Job 2', 'processing_time': 1, 'deadline': 3},
    {'id': 'Job 3', 'processing_time': 3, 'deadline': 8},
    {'id': 'Job 4', 'processing_time': 2, 'deadline': 4},
    {'id': 'Job 5', 'processing_time': 1, 'deadline': 6}
]

# Perform job scheduling
schedule = job_scheduling(jobs)

# Print the schedule
for job in schedule:
    print(f"Job: {job['id']}, Processing Time: {job['processing_time']}, Deadline: {job['deadline']}")

'''class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit

def sortedjobs(job):
    return job.profit

def scheduleJobs(jobs):

    profit = 0

    jobs.sort(key = sortedjobs, reverse = True)
    
    max_deadline = max(job.deadline for job in jobs)

    slots = [-1]*max_deadline

    for job in jobs:
        for i in range(job.deadline-1, -1, -1):
            if slots[i] == -1:
                slots[i] = job.id
                profit += job.profit
                break
    
    print("Sequence: ", end = ' ') 
    for i in range(len(slots)):
        print(f"{slots[i]}", end = ' ')
    return profit


n = int(input("Enter number of jobs: "))

jobs = []

for i in range(n):
    id, profit, deadline = input("Enter id: ").split()
    id = int(id)
    profit = int(profit)
    deadline = int(deadline)
    
    jobs.append(Job(id, deadline, profit))


profit = scheduleJobs(jobs)
print()
print(profit)'''
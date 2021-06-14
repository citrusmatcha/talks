''' Greedy Algorithms: Example 1 - Tasks '''

class Task:
    ''' Represents a task with a start and finish time represented by integers'''
    def __init__(self, name, start, end):
        if end <= start:
            raise Exception("Invalid time range")

        self.name = name
        self.start = start
        self.end = end

    # make it sortable by end time
    def __lt__(self, other):
        return self.end < other.end

    def __repr__(self):
        return str(self.name) + ", start: " + str(self.start) + ", end: " + str(self.end)

def get_max_tasks(task_items):
    ''' The maximum amount of task a person can do such that there are no overlaps '''
    if len(task_items) < 1:
        return 0

    possible_tasks = []
    # Sort the tasks by end time
    task_items.sort()

    # pick the task whose finish time is the earliest
    possible_tasks.append(task_items[0])
    previous_end_time = task_items[0].end

    # for the rest
    for task in task_items:
        if task == possible_tasks[0]:
            continue
        if task.start >= previous_end_time:
            possible_tasks.append(task)
            previous_end_time = task.end

    return len(possible_tasks)

def main():
    ''' Example input '''
    # Your todo list for the day
    schedule = [Task("review PRs", 10, 20), Task("write tests", 12, 25), Task("eat lunch", 20, 30)]

    max_tasks = get_max_tasks(schedule)
    print("With that schedule, you can do a max of ", max_tasks, " tasks!")

if __name__ == "__main__":
    main()

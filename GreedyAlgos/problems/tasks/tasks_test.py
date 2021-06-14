''' Greedy Algorithms: Example 1 - Tasks unit tests'''

import unittest

tasks = __import__("tasks")

class TestGetMaxTasks(unittest.TestCase):
    ''' Get max tasks tests '''

    def test_get_max_tasks(self):
        ''' A happy path test '''
        task_items = [tasks.Task("review PRs", 9, 20), 
                tasks.Task("write tests", 15, 22),
                tasks.Task("eat lunch", 20, 30)]
        num_of_tasks = tasks.get_max_tasks(task_items)
        self.assertEqual(num_of_tasks, 2)

    def test_get_max_tasks_all_overlapping_times(self):
        ''' All items overlap '''
        task_items = [tasks.Task("review PRs", 9, 20), 
                tasks.Task("write tests", 12, 25),
                tasks.Task("eat lunch", 15, 26)]
        num_of_tasks = tasks.get_max_tasks(task_items)
        self.assertEqual(num_of_tasks, 1)

    def test_get_max_tasks_empty_tasks(self):
        ''' Empty tasks '''
        task_items = []
        num_of_tasks = tasks.get_max_tasks(task_items)
        self.assertEqual(num_of_tasks, 0)

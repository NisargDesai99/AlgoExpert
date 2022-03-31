def task_assignment(k, tasks):
	n = len(tasks)
	worker_tasks = []
	task_idx_tracker = {}
	idx = 0
	for task in tasks:
		if task not in task_idx_tracker:
			task_idx_tracker[task] = [idx]
		else:
			task_idx_tracker[task].append(idx)
		idx += 1

	sorted_tasks = sorted(tasks)
	for i in range(k):
		task1 = task_idx_tracker[sorted_tasks[i]].pop()
		task2 = task_idx_tracker[sorted_tasks[n - i - 1]].pop()
		worker_tasks.append([task1, task2])

	return worker_tasks

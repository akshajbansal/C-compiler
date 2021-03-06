void debug_mutex_lock_common(struct mutex *lock, struct mutex_waiter *waiter)
{
	memset(waiter, MUTEX_DEBUG_INIT, sizeof(*waiter));
	waiter->magic = waiter;
	INIT_LIST_HEAD(&waiter->list);
}

void debug_mutex_wake_waiter(struct mutex *lock, struct mutex_waiter *waiter)
{
	lockdep_assert_held(&lock->wait_lock);
	DEBUG_LOCKS_WARN_ON(list_empty(&lock->wait_list));
	DEBUG_LOCKS_WARN_ON(waiter->magic != waiter);
	DEBUG_LOCKS_WARN_ON(list_empty(&waiter->list));
}

void debug_mutex_free_waiter(struct mutex_waiter *waiter)
{
	DEBUG_LOCKS_WARN_ON(!list_empty(&waiter->list));
	memset(waiter, MUTEX_DEBUG_FREE, sizeof(*waiter));
}

void debug_mutex_add_waiter(struct mutex *lock, struct mutex_waiter *waiter,
			    struct task_struct *task)
{
	lockdep_assert_held(&lock->wait_lock);

	/* Mark the current thread as blocked on the lock: */
	task->blocked_on = waiter;
}

void mutex_remove_waiter(struct mutex *lock, struct mutex_waiter *waiter,
			 struct task_struct *task)
{
	DEBUG_LOCKS_WARN_ON(list_empty(&waiter->list));
	DEBUG_LOCKS_WARN_ON(waiter->task != task);
	DEBUG_LOCKS_WARN_ON(task->blocked_on != waiter);
	task->blocked_on = NULL;

	list_del_init(&waiter->list);
	waiter->task = NULL;
}

void debug_mutex_unlock(struct mutex *lock)
{
	if (likely(debug_locks)) {
		DEBUG_LOCKS_WARN_ON(lock->magic != lock);
		DEBUG_LOCKS_WARN_ON(!lock->wait_list.prev && !lock->wait_list.next);
	}
}

void debug_mutex_init(struct mutex *lock, const char *name,
		      struct lock_class_key *key)
{
}

/***
 * mutex_destroy - mark a mutex unusable
 * @lock: the mutex to be destroyed
 *
 * This function marks the mutex uninitialized, and any subsequent
 * use of the mutex is forbidden. The mutex must not be locked when
 * this function is called.
 */
void mutex_destroy(struct mutex *lock)
{
	DEBUG_LOCKS_WARN_ON(mutex_is_locked(lock));
	lock->magic = NULL;
}

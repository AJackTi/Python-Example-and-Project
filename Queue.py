# AJack Ti
# 10/12/2017

class Queue:

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def pop(self):
		return self.items.pop(0)

	def size(self):
		return len(self.items)

	def peek(self):
		return self.items[ len(self.items) - 1 ]

	def push(self, item):
		self.items.append(item)

if __name__ == "__main__":
	q = Queue()
	print "Is empty: " + str(q.isEmpty())
	q.push(1)
	q.push(2)
	q.push(3)
	print "List: " + str(q.items)

	print "Pop item at position 0: " + str(q.pop())
	print "List: " + str(q.items)

	print "Peek of queue: " + str(q.peek())
	print "Size: " + str(q.size())
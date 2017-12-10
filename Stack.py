# AJack Ti
# 10/12/2017

class Stack:

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items) - 1]

	def size(self):
		return len(self.items)

if __name__ == "__main__":
	s = Stack()
	print "Is empty: " + str(s.isEmpty())
	s.push(4)
	s.push('dog')
	s.push(True)
	s.push(8.4)
	print "Peek of Stack: " + str(s.peek())
	print "Items:",
	print s.items
	print "Size: " + str(s.size())
	print "Pop: " + str(s.pop())

	print "Items:",
	print s.items
	print "Size: " + str(s.size())

import itertools
import os
import random
import sys

def create(paths):
	root = TrieNode("")

	curr = root
	for path in paths:
		if path.startswith("/"):
			path = path[1:]
		for component in path.split("/"):
			if component not in curr:
				curr[component] = {}
			curr = curr[component]
		curr = root
	return root

class TrieNode(object):

	def __init__(self, value):
		self.value = value

		self.__children = {}

	def contains(self, path):
		if not path:
			return True

		path = path[1:] if path.startswith("/") else path
		component = "".join(itertools.takewhile(lambda x: x != os.sep, path))
		if component in self.__children:
			return self.__children[component].contains(path[len(component)+1:])
		return False

	def find(self, path):
		if not path:
			return self

		path = path[1:] if path.startswith("/") else path
		component = "".join(itertools.takewhile(lambda x: x != os.sep, path))
		if component in self.__children:
			return self.__children[component].find(path[len(component)+1:])
		return None

	def __getitem__(self, name):
		return self.__children[name]

	def __setitem__(self, name, value):
		self.__children[name] = TrieNode(value)

	def __iter__(self):
		return iter(self.__children)

	def __repr__(self):
		return repr(self.__children)


def create_depth(parent, n, depth):
	if depth < 0:
		return [parent]

	paths = []

	for i in xrange(n):
		name = "a" * 5
		path = os.path.join(parent, name)
		if random.random() > 0.7:
			paths.extend(create_depth(path, n, depth - 1))
		else:
			paths.append(path)
	return paths


def create_test_paths(n, max_depth=10):
	root = "/"

	return create_depth(root, n, max_depth)


def main():
	import time

	paths = create_test_paths(int(sys.argv[1]), int(sys.argv[2]))
	start = time.time()
	root = create(paths)
	print root
	print time.time() - start

if __name__ == "__main__":
	main()

"""
Implements a basic Trie data structure in a simple way
using Python dicts.

The reference implementation is specific to strings. If the program
is run it will create a Trie from the Linux system /usr/share/dict/words and take
one command line argument from the user to search the dictionary of words
that have the user argument as their prefix.

e.g.

python main.py listen

>>> ['listenable',
 'listenings',
 'listens',
 'listenership',
 'listener-in',
 'listened']
"""

import pprint
import sys

DICTIONARY = "/usr/share/dict/words"


def contains(node, word):
	if not word:
		return True

	head = word[0]
	tail = word[1:]

	for char, child in node.items():
		if head == char and contains(child, tail):
			return True

	return False


def traverse(node):
	"""
	Traverse the Trie node depth-first ultimately returning
	the list of words that the node represents.
	"""

	if not node:
		return []

	words = []

	for char, child in node.items():
		child_words = traverse(child)
		if child_words:
			for word in traverse(child):
				words.append(char + word)
		else:
			words.append(char)

	return words


def find(node, prefix):
	"Find the subnode that matches this prefix"

	if not prefix:
		return node

	head = prefix[0]
	tail = prefix[1:]

	if not node:
		return None

	for char, child in node.items():
		if head == char:
			return find(child, tail)

	return None


def build_trie(words):
	root = {}

	curr = root
	for word in words:
		for char in word:
			if char not in curr:
				curr[char] = {}

			curr = curr[char]

		curr = root

	return root


def main():
	try:
		words = open(DICTIONARY).read().splitlines()
	except IOError:
		print "Could not open %s" % DICTIONARY
		sys.exit(1)

	prefix = sys.argv[1]

	root = build_trie(words)

	suffixes = traverse(find(root, prefix))

	pprint.pprint([prefix + suffix for suffix in suffixes])


if __name__ == "__main__":
	main()
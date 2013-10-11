


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

	head = prefix[0]
	tail = prefix[1:]

	if not node:
		return None

	if not tail:
		return node

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
	root = build_trie(["list", "like", "limp"])

	print root

	print traverse(root)

	print contains(root, "like")

	print find(root, "like")


if __name__ == "__main__":
	main()
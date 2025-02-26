import random
from collections import defaultdict, deque
print("Script has started.")

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_word

file_path = 'assets/other/words_alpha.txt'
common_words_file = 'assets/other/corncob_lowercase.txt'

WORD_LIST = Trie()
common_words = set()

# Load common words
try:
    with open(common_words_file, 'r') as file:
        for word in file:
            common_words.add(word.strip().lower())  # Normalize case
except FileNotFoundError:
    print("Common words file not found. Using full dictionary.")

# Load only common three-letter words
try:
    with open(file_path, 'r') as file:
        for word in file:
            word = word.strip().lower()
            if len(word) == 3 and word.isalpha() and word in common_words:
                WORD_LIST.insert(word)
except FileNotFoundError:
    print("Error: Word list file not found.")
    exit()
except Exception as e:
    print(f"Unexpected error: {e}")
    exit()

def valid_word(word):
    return WORD_LIST.search(word)

def one_letter_difference(word1, word2):
    if len(word1) != len(word2):
        return False
    differences = 0
    for c1, c2 in zip(word1, word2):
        if c1 != c2:
            differences += 1
            if differences > 1:
                return False
    return differences == 1

# Extract full words from the Trie
def collect_words(node, prefix="", words=None):
    if words is None:
        words = set()
    if node.is_word and len(prefix) == 3:
        words.add(prefix)
    for char, child in node.children.items():
        collect_words(child, prefix + char, words)
    return words

def build_word_graph(words):
    graph = defaultdict(set)
    word_list = list(words)
    for i, word1 in enumerate(word_list):
        for word2 in word_list:
            if one_letter_difference(word1, word2):
                graph[word1].add(word2)
    return graph

def precompute_reachable_pairs(graph, max_steps=10):
    reachable_pairs_by_distance = defaultdict(list)
    for start_word in graph:
        visited = {start_word: 0}
        queue = deque([(start_word, 0)])
        while queue:
            current_word, steps = queue.popleft()
            if steps < max_steps:
                for neighbor in graph[current_word]:
                    if neighbor not in visited:
                        visited[neighbor] = steps + 1
                        queue.append((neighbor, steps + 1))
        for target_word, distance in visited.items():
            if start_word != target_word:
                reachable_pairs_by_distance[distance].append((start_word, target_word))
    return reachable_pairs_by_distance

all_words = collect_words(WORD_LIST.root)  # Extract real words
graph = build_word_graph(all_words)  # Now correctly build the graph
reachable_pairs_by_distance = precompute_reachable_pairs(graph)

def play_game(start, target):
    if len(start) != len(target):
        print("Words must have the same length.")
        return
    if not valid_word(start) or not valid_word(target):
        print("Start or target word is not valid.")
        return

    print(f"Starting word ladder game: {start} -> {target}")
    current_word = start
    steps = [start]

    while current_word != target:
        next_word = input(f"Current word: {current_word}. Enter next word (or type 'exit' to quit): ").strip().lower()

        if next_word == 'exit':
            print("Game exited by user.")
            return False

        if not valid_word(next_word):
            print("Invalid word. Make sure it's a real word.")
            continue

        if not one_letter_difference(current_word, next_word):
            print("Word must differ by exactly one letter.")
            continue

        steps.append(next_word)
        current_word = next_word

    print(f"Congratulations! You found the path: {' -> '.join(steps)}")
    return True

min_chain_length = 2
while min_chain_length <= max(reachable_pairs_by_distance.keys(), default=10):
    if min_chain_length not in reachable_pairs_by_distance:
        break
    pairs = reachable_pairs_by_distance[min_chain_length]
    if pairs:
        start_word, target_word = random.choice(pairs)
        print(f"New puzzle with chain length {min_chain_length}: {start_word} -> {target_word}")
        if not play_game(start_word, target_word):
            break
        min_chain_length += 1

print("Words in Trie:", len(all_words))
print("Total reachable pairs:", sum(len(v) for v in reachable_pairs_by_distance.values()))
print("Sample words in graph:", list(graph.keys())[:10])

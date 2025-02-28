import random
from collections import defaultdict, deque
import os

print("Script has started.")

# Set the correct file path
file_path = r'C:\Users\dxs788\Downloads\corncob_lowercase.txt' # Adjust if needed

# Check if file exists
if not os.path.exists(file_path):
    print(f"Error: Word list file not found at {file_path}")
    exit()

# Load words into a set
WORD_LIST = set()
try:
    with open(file_path, 'r') as file:
        for word in file:
            word = word.strip().lower()
            if len(word) == 3:  # Only three-letter words
                WORD_LIST.add(word)
except Exception as e:
    print(f"Unexpected error: {e}")
    exit()

print(f"Total 3-letter words loaded: {len(WORD_LIST)}")

def valid_word(word):
    """Check if a word is valid."""
    return word in WORD_LIST

def one_letter_difference(word1, word2):
    """Check if two words differ by exactly one letter."""
    if len(word1) != len(word2):
        return False
    differences = sum(1 for c1, c2 in zip(word1, word2) if c1 != c2)
    return differences == 1

def build_word_graph():
    """Create a graph where words are connected if they differ by one letter."""
    graph = defaultdict(set)
    for word in WORD_LIST:
        for other_word in WORD_LIST:
            if one_letter_difference(word, other_word):
                graph[word].add(other_word)
    return graph

def precompute_reachable_pairs(graph, max_steps=10):
    """Precompute pairs of words based on their shortest transformation distance."""
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

# Build word graph and precompute paths
word_graph = build_word_graph()
reachable_pairs_by_distance = precompute_reachable_pairs(word_graph)

def play_game(start, target):
    """Main gameplay loop."""
    if len(start) != len(target):
        print("Words must have the same length.")
        return False
    if not valid_word(start) or not valid_word(target):
        print("Start or target word is not valid.")
        return False

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

    print(f"🎉 Congratulations! You found the path: {' -> '.join(steps)}")
    return True

# Start with easy puzzles, increasing in difficulty
min_chain_length = 2
while min_chain_length <= max(reachable_pairs_by_distance.keys(), default=10):
    if min_chain_length not in reachable_pairs_by_distance:
        break
    
    pairs = reachable_pairs_by_distance[min_chain_length]
    if pairs:
        start_word, target_word = random.choice(pairs)
        print(f"New puzzle with chain length {min_chain_length}: {start_word} -> {target_word}")
        
        if not play_game(start_word, target_word):
            break  # Exit the game if the user quits
        
        min_chain_length += 1  # Increase difficulty

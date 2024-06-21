# Problem: E - Game is Game - https://codeforces.com/gym/527294/problem/E

import sys
import threading
from sys import stdin

def input(): 
    return stdin.readline().strip()

def main():
    num_strings, num_turns = map(int, input().split())

    trie = {}

    def add_string(string):
        current_node = trie
        for char in string:
            if char not in current_node:
                current_node[char] = {}
            current_node = current_node[char]

    for _ in range(num_strings):
        string = input()
        add_string(string)

    def get_winner(node): 
        # Returns 1 (always wins), -1 (always loses) or 0 (wins or loses)
        can_win = False
        can_lose = False
        for char in node:
            result = get_winner(node[char])
            if result == 1:
                can_win = True
            elif result == -1:
                can_lose = True
            else:
                can_win = can_lose = True

        if not can_win: 
            # If my children always lose, that means I can always win
            return 1
        elif not can_lose: 
            # If my children always win, that means I can always lose
            return -1
        else:
            return 0

    first_player_can_win = False
    first_player_can_lose = False
    for char in trie:
        result = get_winner(trie[char])
        if result == 1:
            first_player_can_win = True
        elif result == -1:
            first_player_can_lose = True

    if first_player_can_win and (num_turns % 2 or first_player_can_lose):
        print("First")
    else:
        print("Second")

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()

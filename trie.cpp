#include <iostream>

using namespace std;

class TrieNode {
public:
    // Initialize your data structure here.
    TrieNode() {
		this->value = '0';
		this->end = false;
		for(size_t i = 0; i < 26; ++i)
		{
			this->sub_nodes[i] = NULL;
		}
    }
	void setEnd() {
		this->end = true;
	}
	void setVal(char c) {
		this->value = c;
	}
	TrieNode* setNthSub(char c) {
		int i = c - 'a';
		if (this->sub_nodes[i] != NULL)
			return this->sub_nodes[i];
		TrieNode* sub = new TrieNode();
		sub->setVal(c);
    	this->sub_nodes[i] = sub;
		return sub;
	}
	TrieNode* getNthSub(char c) {
		int i = c - 'a';
		if (this->sub_nodes[i] != NULL)
			return this->sub_nodes[i];
		return NULL;
	}
	bool isEnd() {
		return this->end;
	}
private:
	char value;
	bool end;
	TrieNode* sub_nodes[26];
};

class Trie {
public:
    Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    void insert(string word) {
		TrieNode* node = this->root;
        for (char& c: word) {
			TrieNode* sub = node->setNthSub(c);
			node = sub;
        }
		node->setEnd();
    }

    // Returns if the word is in the trie.
    bool search(string word) {
		TrieNode* node = this->root;
		for (char& c: word) {
			TrieNode* sub = node->getNthSub(c);
			if (!sub) return false;
			node = sub;
		}
		if (node->isEnd())
			return true;
		return false;
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    bool startsWith(string prefix) {
		TrieNode* node = this->root;
		for (char& c: prefix) {
			TrieNode* sub = node->getNthSub(c);
			if (!sub) return false;
			node = sub;
		}
        return true;
    }

private:
    TrieNode* root;
};

// Your Trie object will be instantiated and called as such:
// Trie trie;
// trie.insert("somestring");
// trie.search("key");

int main (int argc, char const *argv[])
{
	Trie trie;
	trie.insert("something");
	cout << trie.search("something");
	return 0;
}
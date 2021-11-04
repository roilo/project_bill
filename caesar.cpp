#include <iostream>
#include <cctype>
using namespace std;

string encode(string, int);
void decode(string);

int main()
{
	string word;
	int shift;
	char decide;
	
	cout << "enter word: ";
	getline(cin, word);

	do
	{
		cout << "enter shift number: ";
		cin >> shift;
		if ( shift < 26 && shift > 0 )
		{
			word = encode(word, shift);
			cout << word << '\n';
		}
		else
			cout << "Error\n";
	}
	while (shift >= 27 && shift <= -1);
	
	do
	{
		cout << "decode? ";
		cin >> decide;
	}
	while (decide != 'y' && decide != 'n');
	
	if (decide == 'y')
	{
		decode(word);
	}
	system("pause");
	return 0;
}

string encode(string word, int shift)
{
	for (int i = 0; i < word.length(); ++i)
	{
		if (((word[i] + shift) >= 'a' && (word[i] + shift) <= 'z') ||
			((word[i] + shift) >= 'A' && (word[i] + shift) <= 'Z'))
			word[i] += shift;
		else if (word[i] >= 'a' && word[i] <= 'z')
			// word[i] += (shift - ('z' - 'a') - 1);
			word[i] = word[i] + shift - ('z' - 'a') - 1;
		else if (word[i] >= 'A' && word[i] <= 'Z')
			word[i] = word[i] + shift - ('Z' - 'A') - 1;
	}
	return word;
}

void decode(string word)
{
	string code;
	cout << word << '\n';
	for (int i = 1; i < 26; ++i)
	{
		code = word;
		
		for (int j = 0; j < code.length(); ++j)
		{
			if (((code[j] - i) >= 'a' && (code[j] - i) <= 'z' && isalpha(code[j])) ||
				((code[j] - i) >= 'A' && (code[j] - i) <= 'Z' && isalpha(code[j])))
				code[j] -= i;
			else if (code[j] >= 'a' && code[j] <= 'z' && isalpha(code[j]))
				code[j] = code[j] - i + ('z' - 'a') + 1;
				// code[j] -= (i - ('z' + 'a') - 1);
			else if (code[j] >= 'A' && code[j] <= 'Z' && isalpha(code[j]))
				code[j] = code[j] - i + ('Z' - 'A') + 1;
		}
		if (code == word)
			continue;
		cout << "shift " << i << ": " << code << "\n";
		
	}
}

// caesar cipher = (a + b) % 26
// where
// a = plaintext letter
// b = shift number
// a = 0, b = 1, ..., z = 25
// a = 97, z = 122, A = 65, B = 90
// plain text alphabet
// a b c d e f g h i j k l m n o p q r s t u v w x y z
// ex. right shift 3
// d e f g h i j k l m n o p q r s t u v w x y z a b c

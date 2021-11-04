#include <iostream>
#include <cctype>

using namespace std;

string cipher(string);

int main()
{
	string word;
	char decide;
	
	cout << "Word: ";
	getline(cin, word);
	
	cout << "Encode? ";
	cin >> decide;
	decide = tolower(decide);
	
	if (decide == 'y')
	{
		word = cipher(word);
		cout << "Result: " << word << endl;
	}
	
	cout << "Decode? ";
	cin >> decide;
	decide = tolower(decide);
	
	if (decide == 'y')
	{
		word = cipher(word);
		cout << "Result: " << word << endl;
	}
		
	system("pause");
	return 0;
}

string cipher(string word) // encoding is the same as decoding
{
	for (int i = 0; i < word.length(); ++i)
	{
		if (word[i] >= 'a' && word[i] <= 'z' && isalpha(word[i]))
			word[i] = 'z' - word[i] + 'a';
		if (word[i] >= 'A' && word[i] <= 'Z' && isalpha(word[i]))
			word[i] = 'Z' - word[i] + 'A';	
	}
	return word;
}

/*
a = 97, b = 98
z = 122, y = 121
a = z, b = y, ..., z = a;
*/

#include <string>
#include <cctype>
#include <iostream>
using namespace std;

string encodeKey(string, string);
string encodeWord(string, string);
string decode(string, string);

string encodeKey(string word, string key)
{
	int j = word.size();
	
	for (int i = 0; key.size() <= word.size(); i++)
	{
		if (j == i)
			i = 0;
		key.push_back(key[i]);
	}
	return key;
}

string encodeWord(string keyWord, string key)
{
	string code;
	int j;
	
	for (int i = 0; i < keyWord.size(); i++)
	{
		j = 0;
		if (isalpha(keyWord[i]))
		{
			j = (keyWord[i] + key[i]) % 26;
			j += 'A';
			code.push_back(j);
		}
		else
			code.push_back(keyWord[i]);
	}
	return code;
}

string decode(string code, string key)
{
	string word;
	int j = 0;
	
	for (int i = 0; i < code.size(); i++)
	{
		if (isalpha(code[i]))
		{
			j = (code[i] - key[i] + 26) % 26;
			j += 'A';
			word.push_back(j);	
		}
		else
			word.push_back(code[i]);
	}
	return word;
}

int main()
{	
	string word, code, key, keyWord;
	char decision;
	
	cout << "Input: ";
	getline(cin, word, '\n');
	for (int i = 0; i < word.size(); i++)
		word[i] = toupper(word[i]);
	
	cout << "Key: ";
	getline(cin, key, '\n');
	for (int i = 0; i < key.size(); i++)
		key[i] = toupper(key[i]);
	
	do
	{
		cout << "Encode? ";
		cin >> decision;
		decision = tolower(decision);
		cin.ignore(256, '\n');
	}
	while (decision != 'y' && decision != 'n');
	
	if (decision == 'y')
	{
		keyWord = encodeKey(word, key);
		code = encodeWord(word, keyWord);
		cout << "Keyword: " << keyWord << endl;
		cout << "Result: " << code << endl << endl;
	}
	if (decision == 'n')
	{
		system("pause");
		return 0;
	}
	
	do
	{
		cout << "Decode? ";
		cin >> decision;
		decision = tolower(decision);
		cin.ignore(256, '\n');
	}
	while(decision != 'y' && decision != 'n');
	
	if (decision == 'y')
	{
		cout << "Result: " << decode(code, keyWord) << endl << endl;
	}
	system("pause");
	return 0;
}

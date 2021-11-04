#include <iostream>
#include <cctype>
#include <sstream>
using namespace std;

string encode(string);
string decode(string);
bool isPunctuation(char);

string encode(string input)
{
	string str2, temp;
	
    for (int i = 0; i < input.length(); i++)
    {
    	stringstream convert; // i dont understand why this has to initialize everytime
    	temp = "";
    	if (isalpha(input[i]))
    	{
    		convert << (int)(toupper(input[i]) - 'A' + 1); // convert character to int, minus 96
    		convert >> temp; // temp reads convert value, translated to character string
    		str2 += (temp + "-"); // concatenate (?)
		}
		else if (input[i] == ' ')
		{
			if (isPunctuation(input[i-1]))
				str2 += input[i];
			else
				str2 = str2.substr(0, str2.length() - 1) + input[i]; // input[i] is a space
			// we're removing the "-" to acconut for the space
		}
		else if (isPunctuation(input[i]))
		{
			str2 = str2.substr(0, str2.length() - 1) + input[i];
		}
	}
	if (!isPunctuation(str2[str2.length() - 1]))
		str2 = str2.substr(0, str2.length() - 1); // trim off last "-"
	return str2;
}

string decode(string output)
{
	string str2, temp, temp2;
	int temp3;
	
	for (int i = 0; i < (output.length() + 1); i++)
	{
		stringstream convert;
		temp2 = "";
		if (isdigit(output[i]) && output[i+1] != '-') // check if output[i] is a number
		{
			temp += output[i];
		}
		else if (isdigit(output[i]) && output[i+1] == '-') // this only counts the numbers inside, not the blank space
		{
			temp += output[i]; // add tens digit to 
			convert << temp;
			convert >> temp3;
			temp2 = temp3 + 'A' - 1;
			str2 += temp2;
			temp = "";
		}
		else if (output[i] == ' ' || i >= output.length()) // accounts the last letter of encrypted word
		{
			convert << temp;
			convert >> temp3;
			temp2 = temp3 + 'A' - 1;
			if (isPunctuation(output[i-1]))
				str2 += (temp2 + output[i-1] + " ");
			else
				str2 += (temp2 + " ");
			temp = "";
		}
	}
	
	return str2;
}

bool isPunctuation(char input)
{
	return (input == '.'|| input == ',' || input == '!' || input == '?');
}

int main()
{
    string word, code;
    char decision;
    
    cout << "Input: ";
    getline(cin, word, '\n');
    for (int i = 0; i < word.size(); i++)
    	word[i] = toupper(word[i]);
    
    do
    {
    	cout << "Encode? ";
    	cin >> decision;
    	cin.ignore(256, '\n');
	}
	while (decision != 'y' && decision != 'n');
	
	if (decision == 'y')
	{
		code = encode(word);
		cout << "Encrypted: " << code << endl;
	}
	else
	{
		system("pause");
		return 0;
	}
	
	do
    {
    	cout << "Decode? ";
    	cin >> decision;
    	cin.ignore(256, '\n');
	}
	while (decision != 'y' && decision != 'n');
	
	if (decision == 'y')
	{
		word = decode(code);
		cout << "Decrypted: " << word << endl;
	}
	
    system("pause");
    return 0;
}

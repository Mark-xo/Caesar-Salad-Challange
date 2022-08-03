#include <iostream>
#include <string.h>
#include <fstream>
#include <vector>
#include <random>

using namespace std;

int randomNumber() {
    for (int i = 0; i < 1; i++)
        cout << rand() << " ";
}
int main()
{     
    randomNumber();
    return 0;
}


//     string plaintext;
//     string ciphertext;
//     cout << "Enter plaintext: ";
//     getline(cin, plaintext);
//     int key;
//     cout << "Enter key: ";
//     cin >> key;
//     for (int i = 0; i < plaintext.length(); i++)
//     {
//         if (plaintext[i] >= 'a' && plaintext[i] <= 'z')
//             ciphertext += (plaintext[i] + key - 'a') % 26 + 'a';
//         else if (plaintext[i] >= 'A' && plaintext[i] <= 'Z')
//             ciphertext += (plaintext[i] + key - 'A') % 26 + 'A';
//         else
//           ciphertext += plaintext[i];
//     }
//     cout << "Ciphertext: " << ciphertext << endl;

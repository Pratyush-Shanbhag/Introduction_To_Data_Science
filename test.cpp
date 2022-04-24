#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void b() {
    string str = "DFFCXMKGLXQKM ROSRK";
    char a[] = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 
                'Z', ' '};
    for(int i = 0; i < str.size()-3; i++) {
       // if(str[i])
    }
}
int main() {
    ifstream file("encrypt.txt");
    string s;
    getline(file, s);
    cout << s << endl;
    return 0;
}



class FileStream {
    private:
        string filename;
    
    public:
        string readFile() {

        }
};

class Database {};

class Process {};

class OutputStream {};
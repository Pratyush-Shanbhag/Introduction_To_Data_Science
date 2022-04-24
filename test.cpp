#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <tuple>

using namespace std;





class FileStream {
    private:
        string filename;
    
    public:
        FileStream(string inputFile) {
            filename = inputFile;
        }

        string readFile() {
            ifstream file(filename);
            string s;
            getline(file, s);
            return s;
        }
};

class Database {
    private:
        string encrypted;
    
    public:
        Database(string str) {
            encrypted = str;
        }

        string getEncrypted() {
            return encrypted;
        }
};

class Process {
    private:
        string encrypted;
        /*vector<char> a = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
        ' ', '.', ',', ';', '!', '?', '(', ')', '-', '\'', '"'};*/
        vector<string> a = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", ".", ",",
                            ";", "!", "?", "(", ")", "-", "\'", "\""};

        
    
    public:
        Process(string str) {
            encrypted = str;
        }

        void process() {

        }
};

class OutputStream {
    public:
        void run(string str) {
            FileStream fs(str);
            string encrypted = fs.readFile();

            Process p(encrypted);
            p.process();
        }
};


int main() {
    OutputStream os;
    os.run("encrypt.txt");
    return 0;
}
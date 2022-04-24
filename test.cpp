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
        vector<string> a;
        
        unsigned int length;

        vector<int> indices;

        
    
    public:
        Process(Database &db) {
            a =  = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",
                            "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", " ", ".", ",",
                            ";", "!", "?", "(", ")", "-", "\'", "\""};
            
            length = a.size();

            encrypted = db.getEncrypted();
        }

        void process() {
            count();
            findRotorSum();


        }

        int location(char chr) {
            return distance(a.begin(), (find(a.begin(), a.end(), chr)));
        }

        string encrypt(int r1, int r2) {
            string str = "";
            char chr;
            for(int i = 0; i < encrypted.length(); i++) {
                chr = encrypted[i];
                str.append(a[(location(chr) + r1 + r2) % length]);
                r1++;
                if(r1 % length == length - 1) {
                    r2++;
                }
            }
            
            return str;
        }

        void count() {
            int num = 2;
            for(int i = 0; i < 100; i++) {
                if(location(encrypted[i]) + num == location(encrypted[i+num]))
                    indices.push_back(i);
            }
        }

        int findRotorSum() {
            int num1, num2;
            int Aloc = 0;
            int spaceLoc = 36;
            for(unsigned int i = 0; i < indices.size(); i++) {
                num1 = (location(encrypted[i]) - (spaceLoc + i)) % length;
                num1 = num1 < 0 ? num1 + length : num1;
                num2 = (location(encrypted[i + 1]) - (Aloc + i + 1)) % length;
                num2 = num2 < 0 ? num2 + length : num2;
                if(num1 == num2)
                    return num1 - 1;
            }
        }

        

        tuple<string, int, int> decrypt(int rSum) {
            string decrypted;
            int index;
            int n = -1;
            int inc;

            do
            {
                decrypted = "";
                n++;
                inc = 0;
                for(int i = 0; i < encrypted.length(); i++) {
                    if((i + n +1) % length == 0 && i != 0)
                        inc++;
                    index = (location(encrypted[i]) - (rSum + i + inc)) % length;
                    index = index < 0 ? index + length : index;
                    decrypted.append(a[index]);
                }             
            } while (countFrequency(decrypted.substr(0, 99), ". ") != 1);

            return make_tuple(decrypted, n, rSum - n);
        }

        int countFrequency(const string &str, const string &target) {
            int count = 0;
            for(int i = 0; i < str.length() - target.length() + 1; i++) {
                if(str.substr(i, i + target.length() - 1) == target)
                    count++;
            }
            return count;
        }
};

class OutputStream {
    public:
        void run(string str) {
            FileStream fs(str);
            string encrypted = fs.readFile();
            Database db(encrypted);
            Process p(db);
            p.process();
        }
};


int main() {
    OutputStream os;
    os.run("encrypt.txt");
    return 0;
}
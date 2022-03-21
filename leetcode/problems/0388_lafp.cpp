/*
Longest Absolute File Path, https://leetcode.com/problems/longest-absolute-file-path/
The basic idea is to use stack. The challenge of this problem is to analysis string.
*/

#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <string>
#include <map>
using namespace std;

struct File{
    string file_name;
    int file_level;
    bool is_file;
};

class Solution {
private:
    File analysis_file(string token){
        File file;
        int file_level = 0;
        while(token.length() > 1){
            if (token[0] == '\t'){
                token.erase(0, 1);
                file_level += 1;
            }
            else{
                break;
            }
        }
        file.file_name = token;
        file.file_level = file_level;
        file.is_file = (token.find(".") != string::npos);
        return file;
    }

    vector<File> split_input(string input){
        string token;
        string delimiter = "\n"; // split by \n
        vector<File> files;
        int pos = 0;
        while( (pos = input.find(delimiter)) !=  string::npos){
            token = input.substr(0, pos);
            input.erase(0, pos + delimiter.length());
            File file = analysis_file(token);
            files.push_back(file);
        }
        File file = analysis_file(input);
        files.push_back(file);
        return files;
    }

public:
    int lengthLongestPath(string input) {
        return solve(input);
    }

    int solve(string input){
        vector<File> files = split_input(input);
        for(auto file : files){
            cout << file.file_name << ":" << file.is_file << ":" << file.file_level << " ";
        }
        cout << endl;

        vector<File> stack; // only keep the folder
        int res = 0, cur_len = 0; // res is the final result; cur_len stores the length of current folder
        auto file = files.begin();

        while (file != files.end()){
            if (stack.empty() || file->file_level == stack.back().file_level+1){
                if (file->is_file){
                    res = max(res, cur_len+int(file->file_name.length()));
                }
                else{
                    cur_len += (file->file_name.length() + 1);
                    stack.push_back(*file);
                }
                file++;
            }
            else{
                while(!stack.empty() && stack.back().file_level+1 > file->file_level){
                    File top_file = stack.back();
                    stack.pop_back();
                    cur_len -= (top_file.file_name.length() + 1);
                }
            }
        }
        return res;
    }
};

int main(){
    Solution sol;
    // string input = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext";
    // string input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext";
    // string input = "a";
    string input = "file1.txt\nfile2.txt\nlongfile.txt";
    int res = sol.lengthLongestPath(input);
    cout << res << "\n";
    return 0;
}
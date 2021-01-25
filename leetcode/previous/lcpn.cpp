#include <vector>
#include <string>
#include <iostream>

using namespace std;

class Solution {
public:
    string letters[8] = {"abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
    
    // recursive version
    vector<string> letterCombinations(string digits){
        vector<string> result;
        if(digits.length() > 0){
            vector<string> mid_res = letterCombinations(digits.substr(1));
            string letter = letters[digits[0]-'2'];
            for(int i=0; i<(int)letter.length(); i++){
                if(mid_res.size() > 0){
                    for(int j=0; j<(int)mid_res.size(); j++){
                        string new_res = letter[i] + mid_res[j];
                        result.push_back(new_res);
                    }
                }
                else{
                    result.push_back(string(1, letter[i]));    
                }
            }
        }
        return result;
    }

    // iterator version
    vector<string> solve(string digits){
        vector<string> result;
        for(int i=0; i<(int)digits.size(); i++){
            vector<string> mid_res;
            if(result.size() > 0){
                for(int j=0; j<(int)result.size(); j++){
                    string letter = letters[digits[i]-'2'];
                    for(int k=0; k<(int)letter.length(); k++){
                        mid_res.push_back(result[j]+letter[k]);
                    }
                    //mid_res.push_back(result[j]+
                }
                result = mid_res;
            }
            else{
                string letter = letters[digits[i]-'2'];
                for(int j=0; j<(int)letter.size(); j++){
                    result.push_back(string(1, letter[j]));
                }
            }
        }
        return result;
    }
};

int main(){
    string digits = "23";
    Solution ss;
    //vector<string> result = ss.letterCombinations(digits);
    vector<string> result = ss.solve(digits);
    for(int i=0; i<(int)result.size(); i++){
        cout << result[i] << endl;
    }
    return 0;
}

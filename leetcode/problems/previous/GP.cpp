#include <iostream>
#include <string>
#include <vector>

using namespace std;

void printVec(vector<string> vecs){
    for(unsigned i=0; i<vecs.size(); i++){
        cout << vecs[i] << endl;
    }
}

class Solution {
public:
    vector<string> solve(int rest, int pair){
        vector<string> result;
        if(rest == 0 && pair == 0){
            result.push_back("");
        }
        if(rest > 0){
            vector<string> mid_res = solve(rest-1, pair+1);
            for(unsigned i=0; i<mid_res.size(); i++){
                result.push_back("("+mid_res[i]);
            }
        }
        if(pair > 0){
            vector<string> mid_res = solve(rest, pair-1);
            for(unsigned i=0; i<mid_res.size(); i++){
                result.push_back(")"+mid_res[i]);
            }
        }
        return result;
    }

    vector<string> generateParenthesis(int n) {
        int rest_left=n, pair_left=0;
        vector<string> result = solve(rest_left, pair_left);
        return result;
    }
};

int main(){
    Solution ss;
    vector<string> res = ss.generateParenthesis(3);
    printVec(res);
    return 0;
}

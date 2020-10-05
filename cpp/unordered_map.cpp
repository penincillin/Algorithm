/*
 * Group ANagrams: https://leetcode.com/problems/group-anagrams/solution/
 * Hash using unordered_map
 */

#include <iostream>
#include <string>
#include <algorithm>
#include <unordered_map>
#include <vector>
using namespace std;


int main(){
    unordered_map<string, int> map;
    map["abc"] = 1;
    map["cde"] = 2;

    for(auto it=map.begin(); it!=map.end(); it++){
        cout << it->first << " " << it->second << "\n";
    }

    string key = "abc";
    if (map.find(key) != map.end()){
        cout << "find " << key << " " << map[key] << "\n";
    }
    key = "ab";
    if (map.find(key) == map.end()){
        cout << "not find " << key << "\n";
    }

    return 0;
}

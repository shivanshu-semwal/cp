#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    string s;
    cin >> s;
    int ans = 0;
    for (int i = 0; i < n; i++) ans += (s[i] == '0') ? 1 : -1;
    cout << abs(ans);
    return 0;
}
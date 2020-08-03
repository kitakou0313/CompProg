#include <iostream>
#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;
#define MAXSIZE 10000000;

const int MAX = 510000;
const int MOD = 1000000007;
const long long INF = 1LL << 60;

ll dp[10001][1001] = {0};

int main()
{
    string S;

    cin >> S;

    int ansLen = 0;

    set<char> st{'A', 'G', 'C', 'T'};

    for (int i = 0; i < S.size(); i++)
    {
        int tmpLen = 0;
        for (int j = i; j < S.size(); j++)
        {
            if (st.count(S[j]) == 0)
            {
                tmpLen = j - i;
                ansLen = max(ansLen, tmpLen);
                break;
            }

            if (j == S.size() - 1)
            {
                ansLen = max(ansLen, (int)S.size() - i);
                break;
            }
        }
    }

    cout << ansLen << endl;
}

/*Syakutori
while(cin >>b && b)){
      ll t = 1;
      long long int ansS = 1,ansT=0;
      long long int sum = 0;

      for(ll s = 1;s < 50000000;s++){

        while(t <  50000000 && sum+Rsum[t] < b){
          sum += Rsum[t];
          t++;
        }
        if(b == sum+Rsum[t]){
          if(ansT - ansS < t-s){
            ansS = s;
            ansT = t;
          }
          cout <<ansS<<" "<<ansT-ansS + 1<<endl;
          break;
        }
        if(t == s)++t;
        else sum -= Rsum[s];
        }
    }

//priority_queue<long long int,vector<long long int>, greater<long long int>> PQ;
//priority_queue<long long int> PQ1;

bool comp(const pair<int,int> a, const pair<int,int> b) {
    return a.second < b.second;
}

ll gcd(ll a,ll b){
  if(a%b == 0){
    return b;
  }else{
    return gcd(b,a%b);
  }
}


*/

#include <iostream>
#include <bits/stdc++.h>

using namespace std;

typedef long long int ll;
#define MAXSIZE 10000000;

const int MAX = 510000;
const int MOD = 1000000007;
const long long INF = 1LL << 60;

ll dp[10001][1001] ={ 0 };

int main()
{
    int N;
    vector<pair<int, int>>l;
    set<pair<int, int>> st;
    cin >>N;

    int ans = 0;

    for (int i = 0; i < N; i++) {
        int x, y;
        cin >>x>>y;
        l.push_back(make_pair(x, y));
        st.insert(make_pair(x, y));
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (i == j) {
                continue;
            }
            pair<int, int> pi = l[i];
            pair<int, int> pj = l[j];

            pair<int, int> q = make_pair(pi.first -(pj.second - pi.second), pi.second + (pj.first - pi.first));
            pair<int, int> d = make_pair(pj.first -(pj.second - pi.second), pj.second + (pj.first - pi.first));

            if (st.count(q) == 1 and st.count(d) == 1) {
                ans = max(ans, (pi.first - pj.first)*(pi.first - pj.first) + (pi.second - pj.second)*(pi.second - pj.second));
            }
        }
    }

    cout <<ans<<endl;
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

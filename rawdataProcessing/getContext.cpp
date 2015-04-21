#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <map>
#define MP(a, b) make_pair(a, b)
#define PB(a) push_back(a)

using namespace std;
typedef long long ll;
typedef pair<int, int> pii;
typedef pair<unsigned int,unsigned int> puu;
typedef pair<int, double> pid;
typedef pair<ll, int> pli;
typedef pair<int, ll> pil;

const int INF = 0x3f3f3f3f;
const double eps = 1E-6;
const int LEN = 100010;

int main()
{
	freopen("rawDataWithoutFlag.txt", "r", stdin);
	freopen("ripeDataWithoutFlag.txt", "w", stdout);

	char buff[LEN];
	while(cin.getline(buff, LEN, ',')) {
		cin.getline(buff, LEN, ',');
		cin.getline(buff, LEN, ',');
		cout << buff << endl;
		cin.getline(buff, LEN, '\n');
	}
	return 0;
}


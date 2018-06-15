#include <bits/stdc++.h>
using namespace std;
int main(){
	int matrix_rep[10][10]={0};
	for(unsigned int i=0;i<10;i++){
		matrix_rep[i][i]=1;
	}
	cout<< sizeof(matrix_rep)/sizeof(*matrix_rep) << endl;
	for(int i=0;i<10;i++){
		for(int j=0;j<10;j++){
			cout << matrix_rep[i][j];
		}
		cout << endl;
	}
	return 0;
}
#include <bits/stdc++.h>
using namespace std;

struct sparseRepresent{
    int i;
    int j;
    int data;
};

void discreteMatrixDifference(float** a,int row, int column, int n){
    if(n==0){
        return;
    }
    // float returnMat[row][column-1];
    for(int i=0;i<row;i++){
        for(int j=0;j<column-1;j++){
            a[i][j]=a[i][j+1]-a[i][j];
        }
    }
    return discreteMatrixDifference(a, row, column-1, n-1);
}
void printMat(float** a, int row, int column){
    for(int i=0;i<row;i++){
        for(int j=0;j<column;j++){
            cout << a[i][j] << " ";
        }
        cout << endl;
    }
}

vector<sparseRepresent> zeroDiagSparse(float a[], int n){
    vector<sparseRepresent> sparseMatrix;
    sparseRepresent temp;
    for (int i=0;i<n;i++){
        temp.i=i;
        temp.j=i;
        temp.data=a[i];
        sparseMatrix.push_back(temp);
    }
    return sparseMatrix;

}

vector<sparseRepresent> sparseRepresentation(float** a,int row, int col){
    vector<sparseRepresent> sparseMatrix;
    sparseRepresent temp;
    for(int i=0;i<row;i++){
        for(int j=0;j<col;j++){
            if(a[i][j]!=0){
                temp.i=i;
                temp.j=j;
                temp.data=a[i][j];
                sparseMatrix.push_back(temp);
            }
        }
    }
    return sparseMatrix;
}

void printSparse(vector<sparseRepresent> sparseMatrix){
    int n=sparseMatrix.size();
    for(int i=0;i<n;i++){
        cout << sparseMatrix[i].i <<","<< sparseMatrix[i].j <<" "<< sparseMatrix[i].data << endl;
    }
}

int main(){
    float** arr;
    int L=10;
    arr=new float *[L];
    for(int i = 0; i <L; i++)
        arr[i] = new float[L];
    for(int i=0;i<L;i++){
        for(int j=0;j<L;j++){
            if(i==j){
                arr[i][j]=1;
                continue;
            }
            arr[i][j]=0;
        }
    }
    printMat(arr,L,L);
    discreteMatrixDifference(arr,L,L,2);
    printMat(arr,L,L-2);
    printSparse(sparseRepresentation(arr,L,L-2));
    float onesArray[L];
    for(int i=0;i<L;i++){
        onesArray[i]=1;
    }
    cout << "zds"<< endl;
    printSparse(zeroDiagSparse(onesArray, L));


    return 0;
}


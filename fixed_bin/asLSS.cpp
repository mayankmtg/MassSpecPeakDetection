#include <bits/stdc++.h>
using namespace std;

struct sparseRepresent{
    int i;
    int j;
    int data;
};
struct myPair{
    int i;
    int j;
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

vector<sparseRepresent> matrixTranspose(vector<sparseRepresent> mat1){
    vector<sparseRepresent> D=mat1;
    vector<sparseRepresent> Dt;
    for(int i=0;i<mat1.size();i++){
        int temp=D[i].i;
        D[i].i=D[i].j;
        D[i].j=temp;
        Dt.push_back(D[i]);
    }
    return Dt;
}
map<pair<int,int>,int> hashSparseRepresentation(vector<sparseRepresent> mat){
    map<pair<int,int>,int> retMat;
    map<pair<int,int>,int>::iterator itr;
    pair<int,int> x;
    for(int i=0;i<mat.size();i++){
        x=make_pair(mat[i].i, mat[i].j);
        itr=retMat.find(x);
        if(itr==retMat.end()){
            retMat.insert(make_pair(x,mat[i].data));
        }
        else{
            itr->second+=mat[i].data;
        }
    }
    return retMat;
}
void printHashSparse(map<pair<int,int>,int> hSparse){
    map<pair<int,int>,int>::iterator itr;
    for(itr=hSparse.begin();itr!=hSparse.end();itr++){
        cout << itr->first.first<<","<<itr->first.second << " " << itr->second<< endl;
    }
}

// vector<sparseRepresent> matrixSquare(vector<sparseRepresent> mat){
//     vector<sparseRepresent> returnMat;
//     map<pair<int,int>,int> ;


// }
void printSparse(vector<sparseRepresent> sparseMatrix){
    int n=sparseMatrix.size();
    for(int i=0;i<n;i++){
        cout << sparseMatrix[i].i <<","<< sparseMatrix[i].j <<" "<< sparseMatrix[i].data << endl;
    }
}


void computeBaseline(float intensities[], float lambda, float p, int smoothingWindow){
    int L=len(intensities);
    // np.eye as arr
    float** arr;
    arr=new float *[L];
    for(int i = 0; i <L; i++){
        arr[i] = new float[L];
    }
    for(int i=0;i<L;i++){
        for(int j=0;j<L;j++){
            if(i==j){
                arr[i][j]=1;
                continue;
            }
            arr[i][j]=0;
        }
    }
    // np.diff on arr
    discreteMatrixDifference(arr,L,L,2);
    // sparse.csc_matrix as D
    vector<sparseRepresent> D=sparseRepresentation(arr,L,L-2);
    // np.ones as w
    float w[L];
    for(int i=0;i<l;i++){
        w[i]=1.0;
    }

    // W as diagonal matrix spdiags
    vector<sparseRepresent> W;
    
    for(int i=0;i<smoothingWindow;i++){
        W=zeroDiagSparse(w,L);



    }
}

int main(){
    // float** arr;
    // int L=10;
    // arr=new float *[L];
    // for(int i = 0; i <L; i++)
    //     arr[i] = new float[L];
    // for(int i=0;i<L;i++){
    //     for(int j=0;j<L;j++){
    //         if(i==j){
    //             arr[i][j]=1;
    //             continue;
    //         }
    //         arr[i][j]=0;
    //     }
    // }
    // // printMat(arr,L,L);
    // discreteMatrixDifference(arr,L,L,2);
    // // printMat(arr,L,L-2);
    // vector<sparseRepresent> D=sparseRepresentation(arr, L,L-2);
    // float w[L];
    // for(int i=0;i<L;i++){
    //     w[i]=1;
    // }
    return 0;
}
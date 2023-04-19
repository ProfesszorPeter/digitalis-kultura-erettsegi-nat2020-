#include <iostream>
using namespace std;

string parancs, rovid="";
int fdb, vdb, edb, ddb, kdb, ndb;
char v,f;

int main(){
    cout<<"Kerem a robot parancsait: ";
    cin>>parancs;
    edb=0; ddb=0; kdb=0; ndb=0;
    for(int i=0;i<parancs.length();i++)
        switch (parancs[i]){
            case 'E': edb++; break;
            case 'D': ddb++; break;
            case 'N': ndb++; break;
            case 'K': kdb++; break;
        }
    cout<<"E betuk szama: "<<edb<<endl;
    cout<<"D betuk szama: "<<ddb<<endl;
    cout<<"K betuk szama: "<<kdb<<endl;
    cout<<"N betuk szama: "<<ndb<<endl;
    fdb=edb-ddb; vdb=kdb-ndb;
    if (fdb>0)f='E'; else f='D';
    if (vdb>0)v='K'; else v='N';
    for(int i=1;i<=abs(vdb);i++)rovid+=v;
    for(int i=1;i<=abs(fdb);i++)rovid+=f;
    cout<<"A legrovidebb ut parancsszava: "<<rovid<<endl;
    return 0;
}

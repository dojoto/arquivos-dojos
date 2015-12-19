#include "main.cpp"
#include <gtest/gtest.h>
#include <cmath>
#include <sstream>

class ResolveProblema {
public:
  ResolveProblema();

  int tresN(int);
  int iteracao(int, int);
  std::string result(int,int);

};

ResolveProblema::ResolveProblema(){}

int ResolveProblema::tresN(int n) {
  int it = 1;
  while (n!=1){
    if(n%2==0){
      n=n/2;
    }
    else{
      n=(3*n)+1;
    }
    it++;
  }
  return it;
}

int ResolveProblema::iteracao(int i,int j){
  //std::vector<int> ciclos;
  int min = std::min(i,j);
  int max = std::max(i,j);
  int maior = 0;

  for(int i = min; i < max; i++) {
    int comprimentoCiclo = tresN(i);
    if(comprimentoCiclo > maior){
      maior = comprimentoCiclo;
    }

    //ciclos.push_back(comprimentoCiclo);
  }
  return maior;
}

std::string ResolveProblema::result(int i, int j){
  int maior_ciclo = iteracao(i, j);
  std::stringstream ss;
	ss << i << " " << j << " " << maior_ciclo;
  return ss.str();

}


TEST(INPUT, OUTPUT) {
    ResolveProblema resolve;
    //ASSERT_EQ(16, resolve.tresN(22));
    //ASSERT_EQ(20, resolve.iteracao(1,10));
    ASSERT_EQ("10 1 20", resolve.result(10,1));
}

int main(int argc, char **argv) {
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}

#include<iostream>
#include<random>
void generator(char s[28]){



}
int score(char s1[28]){

}
int main(){
	int max=0;
	int count=0;
	char empty_str[28],best[28],generated_str[28];

	for (int i=0;i<28;i++){
		empty_str[i]=' ';
	}

	while(1){
		generator(empty_str);
		generated_str=empty_str
		if (score(generated_str)== 100){
			std::cout<<100;
			break;
		}
		if (score(generated_str)>max){
			max=score(generated_str);
			best=generated_str;
			count++;
		}
		if (count==1000){
			count=0;
			std::cout<<best;
		}


	}
	return 0;



}

	

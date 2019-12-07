#include <iostream>

using namespace std;

//Declaração das funções



int main(){
	int esc;

	cout<<"------ IFCE FORTALEZA ------\n
		   ------ ENG. MECATRÔNICA - VISÃO COMPUTACIONAL\n
		   ------ RODRIGO DOUGLAS BERNARDO DE ARAÚJO\n
		   \n";
	cout<<"DIGITE UMA OPÇÃO PARA INICIAR\n
		   \n
		   ->FILTROS PASSA-BAIXA\n
		   01 - MÉDIA\n
		   02 - MEDIANA\n
		   03 - GAUSSIANO\n
		   \n
		   ->FILTROS PASSA-ALTA\n
		   04 - LAPLACIANO\n
		   05 - PREWIT\n
		   06 - SOBEL\n
		   \n
		   ->OUTRAS OPERAÇÕES\n
		   07 - CALCULO E APRESENTAÇÃO DO HISTOGRAMA\n
		   08 - EQUALIZAÇÃO DO HISTOGRAMA\n
		   09 - LIMIARIZAÇÃO\n
		   10 - MULTILIMIARIZAÇÃO\n
		   \n
		   ESCOLHA:\t";
	cin>>esc;
	switch(esc){
		case 01:
		{
			un();
			break;	
		}
		case 02:
		{
			deux();
			break;
		}
		case 03:
		{
			trois();
			break;
		}
		case 04:
		{
			quatre()
			break;
		}
		case 05:
		{
			cinq();
			break;
		}
		case 06:
		{
			six();
			break;
		}
		case 07:
		{
			sept();
			break;
		}
		case 08:
		{
			huit();
			break;
		}
		case 09:
		{
			neuf();
			break;
		}
		case 01:
		{
			dix();
			break;	
		}
		defaut:
		{
			break;
		}
	}
}

un()
{
	cout<<"01 - MÉDIA\n";
	cout<<"DIGITE O NOME DO ARQUIVO QUE DESEJA APLICAR O FILTRO DA MÉDIA.\n
		   O ARQUIVO DEVE ESTAR NA MESMA PASTA DO PROGRAMA.\n
		   -->\t";
		   
}
deux(){

}
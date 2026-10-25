from dataclasses import dataclass
from time import sleep

@dataclass
class Empresa:
    nome: str
    cidade:str
    segmento: str
    qtd_vendas:int
    qtd_produtos:int
    loja_oficial:bool
    mercado_lider:bool
    
   

    def __str__(self):
        return( f"Nome da Empresa: {self.nome} \nCidade: {self.cidade}\nSegmento: {self.segmento}\nNumero de Vendas: {self.qtd_vendas}\nQuantidade de Produtos: {self.qtd_produtos}")

    def prioridade(self):
        score = self.score_point()
        
        if score >= 5:
            return "Lead de alta prioridade!"
        elif score >= 3:
            return "Lead de média prioridade!"
        else:
            return "Lead de baixa prioridade!"


    def score_point(self):
        score_point = 0

        if self.loja_oficial :
            score_point += 2
        if self.mercado_lider:
            score_point += 1    

        if self.qtd_vendas >= 10000:
            score_point += 3
        elif self.qtd_vendas >= 1000:
             score_point += 2
        else: 
            score_point += 1
        
        return score_point     

def solicitar_inteiro(mensagem):
    while True:
        try:
            num = int(input(mensagem))
            if num < 0:
                print("Digite um valor válido!")
            else:
                return num
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")


def solicitar_texto(mensagem):
    while True:
        texto = input(mensagem).strip()

        if texto == "":
            print("Preencha o campo!")
        else:
            return texto


def solicitar_confirmacao(mensagem):
    while True:
        c = input(mensagem).strip().lower()

        if c == "s":
            return True
        elif c == "n":
            return False
        else:
            print(
                "Resposta inválida. Digite 's' ou 'n'."
            )


        
        
empresas =[]



def criar_empresa():

    encerrar_cadastro = False
    while not encerrar_cadastro:
        
        

            nome = solicitar_texto("Nome da empresa:")
            cidade = solicitar_texto("Cidade da empresa:")
            segmento = solicitar_texto("Segmento da empresa:")
            num_vendas = solicitar_inteiro("Número de vendas da empresa:")
            num_produtos = solicitar_inteiro("Número de produtos da empresa:")    
            loja_oficial = solicitar_confirmacao("Empresa possui loja oficial(s/n): ?")
            mercado_lider = solicitar_confirmacao("Empresa é Mercado Líder: (s/n)?: ")
          
          
            e = Empresa(
                        nome=nome,
                        cidade = cidade,
                        segmento = segmento,
                        qtd_vendas = num_vendas , 
                        qtd_produtos = num_produtos,
                        loja_oficial = loja_oficial,
                        mercado_lider = mercado_lider,
            )      
                    
                    
            print("Empresa adicionada com sucesso!")
            empresas.append(e)

            while True:
                    continuar = input("Deseja cadastrar outra empresa? (s/n): ")
                    if continuar == "s":
                        break
                    elif continuar== "n":
                        print("Encerrando cadastro!")
                        sleep(0.5)
                        encerrar_cadastro = True
                        break
                    else:
                        print(f"O valor digitado {continuar} não é um valor valido por favor digite 's' ou 'n' para esta questão!")
                        sleep(0.7)
                        

    for e in empresas:
        prioridade = e.prioridade()
        score = e.score_point()
        print(e)
        print(f"Prioridade:{prioridade}")
        print(f"Score:{score}")        
        print(f"Loja Oficial:{e.loja_oficial}")        
        print(f"Mercado Líder:{e.mercado_lider}")        

            

if __name__ == "__main__":
    criar_empresa()

                    
                        
                
            

            

                                     
                
                                
                        
                    


         
                
            
                
                
                    
            
                        



            


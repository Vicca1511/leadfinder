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

        
        
empresas =[]



def criar_empresa():

    encerrar_cadastro = False
    while not encerrar_cadastro:
        
        

            nome = input("Digite o nome da empresa:")
            cidade = input("Digite a cidade da empresa:")
            segmento = input("Digite o segmento da empresa:")
            num_vendas = solicitar_inteiro("Digite o numero de vendas da empresa:")
            num_produtos = solicitar_inteiro("Digite o numero de produtos da empresa:")    
          
            while True:

                    loja_oficial = input("Empresa possui loja oficial(s/n): ?").strip().lower()
                    if loja_oficial == "s":
                        loja_oficial = True
                        
                        break
                    elif loja_oficial == "n":
                        loja_oficial = False
                        break
                    else:
                        print(f"O valor digitado {loja_oficial} não é um valor valido por favor digite 's' ou 'n' para está questão!") 
                        
                        
            while True:
               
                    mercado_lider = input("Empresa é Mercado Líder: (s/n)?: ").strip().lower()
                    if mercado_lider == "s":
                        mercado_lider = True
                        break
                    elif mercado_lider == "n":
                        mercado_lider = False
                        break
                    else:
                        print(f"O valor digitado {mercado_lider} não é um valor valido por favor digite 's' ou 'n' para está questão!")
                
                    
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
                    continuar = input("Deseja cadastrar outra empresa? (s/n): ").strip().lower()
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

            
criar_empresa()
                    
                        
                
            

            

                                     
                
                                
                        
                    


         
                
            
                
                
                    
            
                        



            


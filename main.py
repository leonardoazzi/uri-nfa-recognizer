from input_program import leitura, leituraCSV, arg_input
from conversao import afn_para_afd
from automato import AF

def main():
    print("\n////////////////////////////////////////////////////")
    print("AFN->AFD para reconhecimento de sintaxe URI")
    print("Leonardo Azzi Martins e Dennis Pereira Krigger")
    print("////////////////////////////////////////////////////")

    programa_path, palavras_csv_path, opt_lista_rejeita, opt_lista_palavras = arg_input()
    
    alfabeto, estados, transicoes, estado_inicial, estados_finais = leitura(programa_path)

    print(alfabeto, estados, transicoes, estado_inicial, estados_finais)

    afn = AF(alfabeto=alfabeto,
             estados=estados, 
             transicoes=transicoes, 
             estado_inicial=estado_inicial, 
             estados_aceita=estados_finais
            )

    afd = afn_para_afd(afn)

    palavras = leituraCSV(palavras_csv_path)

    if (opt_lista_palavras):
        print("\nPalavras de entrada:")
        for palavra in palavras:
            print('\t', palavra)

    if (opt_lista_rejeita):
        print("\nPalavras do conjunto REJEITA:")
        for palavra in palavras:
            if (afd.aceita(palavra) == False):
                print('\t', palavra)

    print("\nPalavras do conjunto ACEITA:")
    for palavra in palavras:
        if (afd.aceita(palavra)):
            print('\t', palavra)

if __name__ == "__main__":
    main()
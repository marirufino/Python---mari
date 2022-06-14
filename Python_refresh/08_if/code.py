dia_da_semana = input("que dia da semana é hoje? ").lower()

if dia_da_semana == "segunda":
    print("Tenha um bom início de semana!")
elif dia_da_semana == "terça":
    print("É terça!")
else:
    print("Bom resto de semana")

#.lower() faz com que todas as letras se tornem minusculas e não cause erros na comparação 
#pela digitação do usuário

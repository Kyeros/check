emails = []
resposta = "S"

while resposta == "S":
    emails.append(input("Qual é o e-mail vazado? "))
    resposta = input("Deseja cadastras mais e-mails? ")

for email in emails:
    print(email)


# Atividade 6

Esta pasta contém as soluções para a **Atividade 6** de programação. Os exercícios são focados na utilização de módulos nativos do Python e na interação com serviços externos (APIs) para obter dados do mundo real, como perfis de usuários, endereços e cotações de moedas.

---

### 1- Gerador de Senha Aleatória

* Crie um programa que gera uma senha aleatória segura.
* O programa deve utilizar o módulo `random` do Python.
* A senha gerada deve incluir letras maiúsculas, minúsculas, números e caracteres especiais.
* O usuário deve poder especificar o comprimento desejado para a senha.

---

### 2- Gerador de Perfil Aleatório (API)

* Desenvolva um programa que consome a API **'Random User Generator'** para criar um perfil de usuário aleatório.
* O programa deve fazer uma requisição à API e extrair as seguintes informações do resultado:
    * Nome completo
    * E-mail
    * País
* As informações devem ser exibidas de forma clara para o usuário.

---

### 3- Consulta de Endereço por CEP (API)

* Crie um programa que consulta informações de endereço a partir de um CEP.
* O programa deve utilizar a API pública **ViaCEP**.
* O usuário deve informar um CEP, e o programa deve exibir:
    * Logradouro
    * Bairro
    * Cidade
    * Estado
* Deve haver tratamento para o caso de o CEP ser inválido.

---

### 4- Consulta de Cotação de Moeda (API)

* Faça um programa que consulta a cotação atual de uma moeda em relação ao Real (BRL).
* O programa deve utilizar a **AwesomeAPI**.
* O usuário deve informar o código da moeda (ex: **USD**, **EUR**, **GBP**).
* O programa deve exibir:
    * O valor de compra atual (`bid`).
    * A cotação máxima do dia (`high`).
    * A cotação mínima do dia (`low`).
    * A data e hora da última atualização.
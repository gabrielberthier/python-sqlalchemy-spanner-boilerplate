# Inserir um novo produto

## Caso de uso

1. Recebe um schema e o valida
2. Converte em um Dto com dependências (DTO´s também) que é recebido pelo repositório
3. Insere as novas informações e os relacionamentos, se estiverem presentes
4. Retorna o produto salvo com as informações conjuntas

## Cenários

- Deve falhar e retornar 422 quando com um schema inválido [X]
- Deve falhar e retornar 422 com uma subdependência de schema inválida [X]
- Deve falhar e retornar 400 se um produto com mesmo SKU já existir [X]
- Deve falhar e retornar o erro tratado se o repositório falhar [X]
- Deve garantir que o repositório será chamado
- Deve inserir o novo produto via repositório
- Deve retornar o novo produto via repositório

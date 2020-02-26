# Periodic Table - React e FastAPI `:seedling:`

Este é um projeto que venho levando há algum tempo, que fiz para que uma amiga que faz bacherelado em química pudesse consultar alguns elementos pelo celular ou computador (emocionante não?), bem fiz como estudo então algumas decisões de projeto foram feitas somente para aprendizado de alguma tecnologia como GraphQL, FastAPI e React. Há alguns pontos que devo melhorar com o passar do tempo e outras refazer totalmente, como o banco de dados, sem mais enrolação vou esclarecer alguns pontos da arquitetura do projeto caso esteja curioso.

### Backend

O backend foi feito em python com o framework [FastAPI](https://fastapi.tiangolo.com/) que trata todas as requisições do frontend, e também mantém o GraphQL no ar o qual usei a biblioteca [Graphene](https://graphene-python.org/) para criar.

### Frontend

No Frontend usei o [Bulma](https://bulma.io/) como framework CSS o qual é bem bonito, moderno, fácil de utilizar e não deixa o app em minha opinião tão processada quanto o Bootstrap, foi utilizada a bibilioteca do [React](https://pt-br.reactjs.org/) e gostei bastante do esquema de components e de states que facilitam e que me deram bastante liberdade ao fazer o app, foi a primeira vez que utilizei então sou suspeito para falar.
![alt text](https://xandev.codes/content/images/2020/02/mobile-menu.png)
![alt text](https://xandev.codes/content/images/2020/02/graphQL.png)

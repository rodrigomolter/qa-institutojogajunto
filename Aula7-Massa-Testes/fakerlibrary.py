from faker import Faker

faker = Faker('pt_BR')

persona = {
  "nome" : faker.name(),
  "idade" : faker.random_int(min=18, max=99),
  "cidade" : faker.city()
}

print(persona)
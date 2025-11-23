describe('Carrinho - adicionar e finalizar compra', () => {
  const username = 'cart_user'
  const email = 'cart_user@example.com'
  const password = 'TestPass123!'

  before(() => {
    cy.ensureUser(username, email, password)
  })

  it('adiciona um livro ao carrinho e finaliza a compra', () => {
    cy.login(username, password)

    cy.visit('/')

    cy.get('.card-title').first().then($link => {
      cy.wrap($link).click()
    })

    cy.contains('Adicionar ao Carrinho').click()

    cy.url().should('include', '/carrinho')

    cy.get('.cart-container').should('exist')
    cy.contains('Finalizar Compra').should('exist')

    cy.contains('Finalizar Compra').click()

    cy.contains('Seu carrinho está vazio').should('exist')
  })
})
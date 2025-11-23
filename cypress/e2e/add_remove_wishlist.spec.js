describe('Add and remove wishlist', () => {
  const username = 'wish_user'
  const email = 'wish_user@example.com'
  const password = 'TestPass123!'

  before(() => {
    cy.ensureUser(username, email, password)
  })

  it('adds and removes a book from wishlist', () => {
    cy.login(username, password)

    // go to book list
    cy.visit('/')

    // add first book to wishlist from its card
    cy.get('.book-card').first().within(() => {
      cy.contains('Adicionar aos Desejos').click()
    })

    // open wishlist page and remove the item
    cy.visit('/lista-de-desejos/')
    cy.contains('Remover').first().click()

    // after removal, the remove link should not exist
    cy.contains('Remover').should('not.exist')
  })
})

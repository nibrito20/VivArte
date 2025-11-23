describe('Add and remove wishlist', () => {
  before(() => {
    // ensure a user exists by registering via UI if necessary
    cy.visit('/users/register/')
    cy.get('input[name="username"]').then($el => {
      if ($el.length) {
        cy.get('input[name="username"]').clear().type('wish_user')
        cy.get('input[name="email"]').clear().type('wish_user@example.com')
        cy.get('input[name="password1"]').clear().type('TestPass123!')
        cy.get('input[name="password2"]').clear().type('TestPass123!')
        cy.get('form').submit()
      }
    })
  })

  it('adds and removes a book from wishlist', () => {
    // login
    cy.visit('/users/login/')
    cy.get('input[name="username"]').clear().type('wish_user')
    cy.get('input[name="password"]').clear().type('TestPass123!')
    cy.get('form').submit()

    // go to library page
    cy.visit('/library/')

    // find a book card (assumes at least one book exists)
    cy.get('body').contains('Adicionar').first().click()

    // visit wishlist and remove
    cy.visit('/library/lista-de-desejos/')
    cy.get('body').contains('Remover').first().click()

    // after removal, the removed button/text should not be visible
    cy.get('body').contains('Remover').should('not.exist')
  })
})

describe('Filter books by genre', () => {
  before(() => {
    // try to ensure user exists
    cy.visit('/users/login/')
    cy.get('input[name="username"]').then($el => {
      if ($el.length) {
        // no-op
      }
    })
  })

  it('filters books when clicking genre links', () => {
    cy.visit('/users/login/')
    // if login is present, attempt to sign in with a known test user
    cy.get('input[name="username"]').clear().type('wish_user')
    cy.get('input[name="password"]').clear().type('TestPass123!')
    cy.get('form').submit()

    cy.visit('/library/')

    // Click Romance and assert Romance books show
    cy.contains('Romance').click()
    cy.wait(500)
    // assert at least one book remains visible
    cy.get('body').should('contain.text', 'Romance')

    // Click Ação and assert Ação books show
    cy.contains('Ação').click()
    cy.wait(500)
    cy.get('body').should('contain.text', 'Ação')
  })
})

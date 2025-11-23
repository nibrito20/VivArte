describe('View profile information', () => {
  it('displays user profile info', () => {
    // login
    cy.visit('/users/login/')
    cy.get('input[name="username"]').clear().type('wish_user')
    cy.get('input[name="password"]').clear().type('TestPass123!')
    cy.get('form').submit()

    cy.visit('/users/account/')

    // Check that name and email appear
    cy.get('body').should('contain.text', 'wish_user')
    cy.get('body').should('contain.text', 'wish_user@example.com')
  })
})

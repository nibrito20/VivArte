describe('Register and Login flow', () => {
  it('allows a user to register and login', () => {
    cy.visit('/users/register/')

    cy.get('input[name="username"]').clear().type('cypress_user')
    cy.get('input[name="email"]').clear().type('cypress_user@example.com')
    cy.get('input[name="password1"]').clear().type('TestPass123!')
    cy.get('input[name="password2"]').clear().type('TestPass123!')

    cy.get('form').submit()

    // After registration the site may show a link to login or redirect
    cy.visit('/users/login/')

    cy.get('input[name="username"]').clear().type('cypress_user')
    cy.get('input[name="password"]').clear().type('TestPass123!')
    cy.get('form').submit()

    // Confirm that logout or account is visible in the UI
    cy.contains('Sair').should('exist')
  })
})

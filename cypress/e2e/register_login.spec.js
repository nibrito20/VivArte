describe('Register and Login flow', () => {
  const username = 'cypress_user'
  const email = 'cypress_user@example.com'
  const password = 'TestPass123!'

  it('ensures user exists and can login', () => {
    // Ensure the user exists (will try login first, then register if needed)
    cy.ensureUser(username, email, password)

    // Explicitly test the login flow
    cy.login(username, password)

    // Confirm that logout or account is visible in the UI
    cy.contains('Sair').should('be.visible')
  })
})

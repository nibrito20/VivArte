describe('View profile information', () => {
  const username = 'profile_user'
  const email = 'profile_user@example.com'
  const password = 'TestPass123!'

  before(() => {
    cy.ensureUser(username, email, password)
  })

  it('displays user profile info', () => {
    cy.login(username, password)

    cy.visit('/users/account/')

    // Check that username and email appear
    cy.contains(username).should('exist')
    cy.contains(email).should('exist')
  })
})

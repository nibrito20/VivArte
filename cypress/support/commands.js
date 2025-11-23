// Custom Cypress commands for the VivArte project

// Simple login command used across tests
Cypress.Commands.add('login', (username, password) => {
  cy.visit('/users/login/')
  cy.get('input[name="username"]').clear().type(username)
  cy.get('input[name="password"]').clear().type(password)
  cy.get('form').submit()
})

// Command to ensure test user exists by registering via UI (idempotent for our flows)
Cypress.Commands.add('ensureUser', (username, email, password) => {
  cy.visit('/users/register/')
  cy.get('body').then($body => {
    // If registration form exists, create the user
    if ($body.find('input[name="username"]').length) {
      cy.get('input[name="username"]').clear().type(username)
      cy.get('input[name="email"]').clear().type(email)
      cy.get('input[name="password1"]').clear().type(password)
      cy.get('input[name="password2"]').clear().type(password)
      cy.get('form').submit()
    }
  })
})

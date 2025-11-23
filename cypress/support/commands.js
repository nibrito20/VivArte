// Custom Cypress commands for the VivArte project

// Simple login command used across tests
Cypress.Commands.add('login', (username, password) => {
  cy.visit('/users/login/')
  cy.get('input[name="username"]').clear().type(username)
  cy.get('input[name="password"]').clear().type(password)
  // click the visible submit button to match the template which uses a button element
  cy.get('button.form-submit, button.login-button, button[type="submit"]').filter(':visible').first().click()

  // Wait for Django session cookie to be set and for UI to reflect logged-in state
  cy.getCookie('sessionid', { timeout: 10000 }).should('exist')
  // Prefer checking for a visible logout link or 'Sair' text
  cy.contains('Sair', { timeout: 10000 }).should('be.visible')
})

// Command to ensure test user exists by registering via UI (idempotent for our flows)
Cypress.Commands.add('ensureUser', (username, email, password) => {
  // Try to login first - if login works, don't attempt to register
  cy.visit('/users/login/')
  cy.get('body').then($body => {
    if ($body.find('input[name="username"]').length) {
      cy.get('input[name="username"]').clear().type(username)
      cy.get('input[name="password"]').clear().type(password)
      cy.get('button.form-submit, button.login-button, button[type="submit"]').filter(':visible').first().click()

      // If login succeeded (session cookie or logout visible), we're done
      cy.getCookie('sessionid', { timeout: 5000 }).then(cookie => {
        if (cookie) {
          return
        }

        // otherwise try registration
        cy.visit('/users/register/')
        cy.get('body').then($body2 => {
          if ($body2.find('input[name="username"]').length) {
            cy.get('input[name="username"]').clear().type(username)

            // fill first and last name if present
            if ($body2.find('input[name="first_name"]').length) {
              const parts = username.split('_')
              const first = parts[0] ? parts[0] : 'Test'
              const last = parts[1] ? parts[1] : 'User'
              cy.get('input[name="first_name"]').clear().type(first)
              if ($body2.find('input[name="last_name"]').length) {
                cy.get('input[name="last_name"]').clear().type(last)
              }
            }

            cy.get('input[name="email"]').clear().type(email)
            cy.get('input[name="password1"]').clear().type(password)
            cy.get('input[name="password2"]').clear().type(password)
            cy.get('button[type="submit"], button.form-submit').filter(':visible').first().click()

            // wait for registration/login to complete
            cy.getCookie('sessionid', { timeout: 10000 }).should('exist')
          }
        })
      })
    } else {
      // No login form - maybe already logged in or different route; ensure session cookie present
      cy.getCookie('sessionid', { timeout: 5000 }).should('exist')
    }
  })
})

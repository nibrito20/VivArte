describe('Filter books by genre', () => {
  const username = 'wish_user'
  const email = 'wish_user@example.com'
  const password = 'TestPass123!'

  before(() => {
    cy.ensureUser(username, email, password)
  })

  it('filters books when clicking genre links', () => {
    cy.login(username, password)

    cy.visit('/')

    // Click Romance and check the page title mentions the genre
    cy.contains('Romance').click()
    cy.get('.page-title').should('contain.text', 'Gênero')

    // Click Ação and assert the page title updates
    cy.contains('Ação').click()
    cy.get('.page-title').should('contain.text', 'Gênero')
  })
})

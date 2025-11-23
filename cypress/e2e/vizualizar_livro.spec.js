describe('View book detail', () => {
  it('opens the first book detail and verifies the title', () => {
    cy.visit('/')

    // wait for the book list to render and grab the first book title
    cy.get('.card-title', { timeout: 10000 }).first().then($el => {
      const title = $el.text().trim()
      // click the book link
      cy.wrap($el).click()

      // on the detail page the main h1 should contain the same title
      cy.get('h1', { timeout: 10000 }).should('contain.text', title)
    })
  })
})

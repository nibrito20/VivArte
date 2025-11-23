describe('View book detail', () => {
  it('navigates to a book detail page and checks the title', () => {
    cy.visit('/')
    cy.contains('Biblioteca').click()
    cy.contains('Harry Potter e a Pedra Filosofal').click()
    cy.get('h1').should('contain.text', 'Harry Potter e a Pedra Filosofal')
  })
})

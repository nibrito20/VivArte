describe('Submit review', () => {
  const username = 'wish_user'
  const email = 'wish_user@example.com'
  const password = 'TestPass123!'

  before(() => {
    cy.ensureUser(username, email, password)
  })

  it('submits a review for a book', () => {
    cy.login(username, password)

    // navigate to first book detail
    cy.visit('/')
    cy.get('.card-title').first().click()

    // submit a review if form exists
    cy.get('form').within(() => {
      cy.get('input[name="subject"]').clear().type('Incrível leitura!')
      cy.get('textarea[name="review"]').clear().type('Gostei muito deste livro, super recomendo!')
      cy.get('input[name="rating"][value="5"]').check({force: true})
      cy.get('input.btn-submit, button[type="submit"]').first().click()
    })

    // after submit the review subject should be visible in reviews
    cy.contains('Incrível leitura!').should('exist')
  })
})

describe('The Home Page', function() {
    it('successfully loads', function() {
      cy.visit('http://localhost:5000/SignUp') // change URL to match your dev URL
      cy.get('[placeholder="Username"]').type('test_cypress')
      cy.get('[placeholder="Email"]').type('testcypress@company.com')
      cy.get('[type="password"]').type('12345678')
      cy.get('button').click()

      cy.get('h2').should('have.value', 'Sign up failed')

    })



  })
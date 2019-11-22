describe('Successful SignUp Test', function() {
    it ('Tests sign up to make sure it works', function() {
        cy.visit('http://localhost:5000/SignUp')
        cy.get('#uname').type('test_username')
        cy.get('#email').type('myemail'+Math.random()+'@gmail.com')
        cy.get('#psw').type('12345678')
        cy.get('#submit').click()
        cy.get('#success')
    });
}
);

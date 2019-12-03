<!-- Given-When-Then (GWT) User Acceptance Tests

Scenario: OBS needs to display stock prices to users.
Given: Stocks with changing values.
When: The user opens or refreshed the dashboard..
Then: The most up to date stock prices will be displayed to the user.

Scenario: OBS wants to be able to track its client’s assets.
Given: The clients has stocks and cash to monitor.
When: A user buys/sells stocks.
Then: The correct account is debited and the correct account is credited. 

Scenario: An authorized user is signing up for multiple accounts.
Given: Bob already has three accounts.
When: Bob is attempting to sign up for another account.
Then: Return an error.

Scenario: An authorized user wants to make money with the OBS.
Given: An authorized user is attempting to buy and sell stocks.
When: An authorized user buys or sells a valid amount of stocks.
Then: Add or subtract values from the bank and the user.

Scenario: An authenticated client Bob wants to access his dashboard.
Given: Bob already has an OBS account or is willing to create a new account.
When: Bob opens the “Login” or “Registration” pages, correctly inputs his information, and clicks the submit button.
Then: Bob is taken to his dashboard.

Scenario: Authenticated-Bob wants to add funds to his account
Given: Bob already has an OBS account AND is logged into his account.
When: Bob clicks on “Add Funds” he goes to a page where he can enter an amount of money AND select the account to add money AND click submit. 
Then: Bob sees a confirmation page that confirms he added the money to his account AND after a bit is redirected back to his dashboard

Scenario: Authenticated-Bob is trying to buy more stocks but does not have sufficient funds in his account.
Given: Bob already has an OBS account AND is logged in AND has less money in his account than the price of the stock he is trying to buy.
When: Bob clicks on “Buy <stock>”, a message will pop up saying he does not have sufficient funds AND asks him if he would like to add more funds right now.
Then: Bob will be redirected to the “Add Funds To Account” page. 

Scenario: Non-authenticated user Bob attempts to access the dashboard or perform a stock transaction.
Given: Bob is not logged in to his OBS account or does not have an OBS account.
When: Bob tries to enter the “Dashboard” page or tries to perform a stock transaction.
Then: An error message appears telling Bob that he needs to be logged in to access those functionalities.

Scenario: Unauthenticated-Bob is trying to log into his account.
Given: Bob has memory issues and cannot remember his username/password for his account. 
When: Bob tries to log into the account with the incorrect login information.
Then: An error message appears saying the username/password is incorrect. 

Scenario:  A new client Bob wants to register for his new OBS account.
Given: Bob does not already have an OBS account and is not authenticated.
When: Bob goes to the “Registration” page, correctly inputs valid information for all the required fields, and clicks the submit button.
Then: A message tells Bob that the registration was successful and then Bob is logged and taken to his dashboard.

Scenario: Bob sees a great opportunity and in his haste tries to purchase stocks worth more than in his account. 
Given: Bob has $2 in his account.
When: Bob attempts a purchase of $400.
Then: Bob will see an error message saying he does not have sufficient funds AND be prompted to add more money to their account.

Scenario: Bob wants to add a second bank account to his account to be able to transfer funds from his various banks.
Given: Bob is signed in to his stock account with his valid login credentials.
When: Bob tries to add information for a different bank account, with at least one bank account already accessible.
Then: Bob is able to successfully add the bank account information as a source of funds to his stock trading account. -->

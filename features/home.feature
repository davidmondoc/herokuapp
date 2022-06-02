Feature: herokuapp home page link tests
  Background:
    Given herokuapp home: i am testing herokuapp


    Scenario: i am testing if links on herokuapp respond when clicked
      When checking form
      When checking basic
      When checking digest
      When checking download
      When checking upload
#      Then last ckeck
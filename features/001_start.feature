# Created by viktor at 2019-08-29
@start
Feature: Test feature
  # Enter feature description here

  @smoke
  Scenario: Test GET scenario
    Given send "get" to url "https://www.google.com" with json "{}"
    Then check response code is "400"

  @smoke
  Scenario: Test POST scenario
    Given send "post" to url "http://localhost:5000/post" with json "{"name":"testaasadfasad","salary":"123","age":"23"}"
    Then check response code is "200"

  @smoke
  Scenario: Test JSONPATH ASSERTION scenario
    Given send "get" to url "http://dummy.restapiexample.com/api/v1/employees" with json "{}"
    Then check response code is "200"
    And check response body has param "status"
    And check response body has param "status" with value "success"
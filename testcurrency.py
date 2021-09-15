"""
Unit tests for module currency

When run as a script, this module invokes several procedures that test
the various functions in the module currency.

Author: Sidney G. Cole, Jr.
Date:   2 September 2021
"""

import introcs
import currency

def test_before_space():
    """
    
    Test procedure for before_space.
    
    """
    
    print('Testing before_space')
    
    #Test 1
    result=currency.before_space('Hello World')
    introcs.assert_equals('Hello', result)
    
    #Test 2
    result=currency.before_space(' HelloWorld')
    introcs.assert_equals('', result)
    
    #Test 3
    result=currency.before_space('Hello  World')
    introcs.assert_equals('Hello', result)
    
    #Test 4
    result=currency.before_space('Hello World ')
    introcs.assert_equals('Hello', result)
    
    
def test_after_space():
    """
    
    Test procedure for after_space
    
    """
    
    print('Testing after_space')
    
    #Test 1
    result=currency.after_space('Hello World')
    introcs.assert_equals('World', result)
    
    #Test 2
    result=currency.after_space(' Hello World')
    introcs.assert_equals('Hello World', result)
    
    #Test 3
    result=currency.after_space('Hello  World')
    introcs.assert_equals(' World', result)
    
    #Test 4
    result=currency.after_space('HelloWorld ')
    introcs.assert_equals('', result)
    
    
def test_first_inside_quotes():
    """
    
    Test procedure for first_inside_quotes
    
    """
    
    print('Testing first_inside_quotes')
    
    #Test 1
    result=currency.first_inside_quotes('A "BC" D')
    introcs.assert_equals('BC', result)
    
    #Test 2
    result=currency.first_inside_quotes('A "BC" D "EF" G')
    introcs.assert_equals('BC', result)
    
    #Test 3
    result=currency.first_inside_quotes('"ABCDE"')
    introcs.assert_equals('ABCDE', result)
    
    #Test 4
    result=currency.first_inside_quotes('A "" BCD')
    introcs.assert_equals('', result)
    
  
def test_get_src():
    """
    
    Test procedure for get_src
    
    """
    
    print('Testing get_src')
    
    #Test 1
    result=currency.get_src('{"success": true, "src": "2 United States Dollars",'+
                            '"dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars', result)
    
    #Test 2
    result=currency.get_src('{"success":false,"src":"","dst":"","error":"Source '+
                            'currency code is invalid."}')
    introcs.assert_equals('', result)
    
    #Test 3 
    result=currency.get_src('{"success":false,"src": "","dst":"","error":"Source '+
                            'currency code is invalid."}')
    introcs.assert_equals('', result)
    
    #Test 4
    result=currency.get_src('{"success": true, "src":"2 United States Dollars", '+
                            '"dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('2 United States Dollars', result)
    
    
def test_get_dst():
    """
    
    Test procedure for get_dst
    
    """
    
    print('Testing get_dst')
    
    #Test 1
    result=currency.get_dst('{"success": true, "src": "2 United States Dollars",'+
                            '"dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros', result)
    
    #Test 2
    result=currency.get_dst('{"success":false,"src":"","dst":"","error":"Source '+
                            'currency code is invalid."}')
    introcs.assert_equals('', result)
    
    #Test 3
    result=currency.get_dst('{"success":false,"src":"","dst": "","error":"Source'+
                            ' currency code is invalid."}')
    introcs.assert_equals('', result)
    
    #Test 4
    result=currency.get_dst('{"success": true, "src": "2 United States Dollars",'+
                            ' "dst":"1.772814 Euros", "error": ""}')
    introcs.assert_equals('1.772814 Euros', result)
    
    
def test_has_error():
    """
    
    Test procedure for has_error
    
    """
    
    print('Testing has_error')
    
    #Test 1
    result=currency.has_error('{"success":false,"src":"","dst":"","error":"Sourc'+
                              'e currency code is invalid."}')
    introcs.assert_equals(True, result)
    
    #Test 2
    result=currency.has_error('{"success": true, "src": "2 United States Dollars'+
                              '", "dst": "1.772814 Euros", "error": ""}')
    introcs.assert_equals(False, result)
    
    #Test 3
    result=currency.has_error('{"success":true, "src":"2 United States Dollars",'+
                              ' "dst":"1.772814 Euros", "error":""}')
    introcs.assert_equals(False, result)
    
    #Test 4
    result=currency.has_error('{"success":false,"src":"","dst":"","error": "Sour'+
                              'ce currency code is invalid."}')
    introcs.assert_equals(True, result)
    
    
def test_service_response():
    """
    
    Test procedure for service_response
    
    """
    
    print('Testing service_response')
    
    #Test 1
    input=currency.service_response('USD','EUR',2.5)
    introcs.assert_equals('{"success": true, "src": "2.5 United States Dollars",'+
                          ' "dst": "2.2160175 Euros", "error": ""}', input)
    
    #Test 2
    input=currency.service_response('USD','EUR',-2.5)
    introcs.assert_equals('{"success": true, "src": "-2.5 United States Dollars"'+
                          ', "dst": "-2.2160175 Euros", "error": ""}', input)
    
    #Test 3
    input=currency.service_response('DSU','EUR',2.5)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error": "Th'+
                          'e rate for currency DSU is not present."}', input)
    
    #Test 4
    input=currency.service_response('USD','DSU',2.5)
    introcs.assert_equals('{"success": false, "src": "", "dst": "", "error": "Th'+
                          'e rate for currency DSU is not present."}', input)
    
    
def test_iscurrency():
    """
    
    Test procedure for iscurrency
    
    """
    
    print('Testing iscurrency')
    
    #Test 1
    result=currency.iscurrency('USD')
    introcs.assert_equals(True, result)
    
    #Test 2
    result=currency.iscurrency('US')
    introcs.assert_equals(False, result)
    
    
def test_exchange():
    """
    Test procedure for exchange
    
    """
    
    print('Testing exchange')
    
    #Test 1
    result=currency.exchange('USD', 'EUR', 2.5)
    introcs.assert_floats_equal(result, result)
    
    #Test 2
    
    result=currency.exchange('USD', 'EUR', -2.5)
    introcs.assert_floats_equal(result, result) 


#Script Code
test_before_space()
test_after_space()
test_first_inside_quotes()
test_get_src()
test_get_dst()
test_has_error()
test_service_response()
test_iscurrency()
test_exchange()

print('All tests completed successfully')
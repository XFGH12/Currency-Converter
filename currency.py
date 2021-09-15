"""
Module for currency exchange

This module provides several string parsing functions to implement a simple
currency exchange routine using an online currency service. The primary function
in this module is exchange().

Author: Sidney G. Cole, Jr.
Date:   2 September 2021
"""

import introcs

APIKEY='ueIF8BxNAM0BbGgqZwCp8pKdhAFAl6QLGy64srrBDXEe'

def before_space(s):
    """
Returns the substring of s up to, but not including, the first space.

Example: before_space('Hello World') returns 'Hello'

Parameter s: the string to slice
Precondition: s is a string with at least one space in it

    """
    
    assert type(s)==str, 'Not a string'
    assert introcs.count_str(s, " ")>=1, 'Needs at least 1 space'
    
    space1=introcs.index_str(s, ' ')
    bspace=(s[:space1])
    return bspace


def after_space(s):
    """
Returns the substring of s after the first space

Example: after_space('Hello World') returns 'World'

Parameter s: the string to slice
Precondition: s is a string with at least one space in it

    """
    
    assert type(s)==str, 'Not a string'
    assert introcs.count_str(s, " ")>=1, 'Needs at least 1 space'
    
    space2=introcs.index_str(s, ' ')
    aspace=(s[space2+1:])
    return aspace


def first_inside_quotes(s):
    """
Returns the first substring of s between two (double) quote characters

Note that the double quotes must be part of the string.  So "Hello World" is a 
precondition violation, since there are no double quotes inside the string.

Example: first_inside_quotes('A "B C" D') returns 'B C'
Example: first_inside_quotes('A "B C" D "E F" G') returns 'B C', because it only 
picks the first such substring.

Parameter s: a string to search
Precondition: s is a string with at least two (double) quote characters inside

    """
    
    assert type(s)==str, 'Not a string'
    assert introcs.count_str(s, '"')>=2, 'Needs at least 2 sets of quotes'
    
    start=introcs.index_str(s, '"')
    end=introcs.index_str(s, '"', start+1)
    inside=(s[start+1:end])
    return inside


def get_src(json):
    """
Returns the src value in the response to a currency query.

Given a JSON string provided by the web service, this function returns the string
inside string quotes (") immediately following the substring '"src"'. For example,
if the json is
    
    '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

then this function returns '2 United States Dollars' (not '"2 United States Dollars"'). 
On the other hand if the json is 
    
    '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

then this function returns the empty string.

The web server does NOT specify the number of spaces after the colons. The JSON
    
    '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
    
is also valid (in addition to the examples above).

Parameter json: a json string to parse
Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    
    assert type(json)==str, 'Not a string'
    
    
    start=introcs.rfind_str(json, '"src":')
    result=(json[start+5:])
    value=(first_inside_quotes(result))
    return value


def get_dst(json):
    """
Returns the dst value in the response to a currency query.

Given a JSON string provided by the web service, this function returns the string
inside string quotes (") immediately following the substring '"dst"'. For example,
if the json is
    
    '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

then this function returns '1.772814 Euros' (not '"1.772814 Euros"'). On the other
hand if the json is 
    
    '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

then this function returns the empty string.

The web server does NOT specify the number of spaces after the colons. The JSON
    
    '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
    
is also valid (in addition to the examples above).

Parameter json: a json string to parse
Precondition: json a string provided by the web service (ONLY enforce the type)
    """
    
    assert type(json)==str, 'Not a string'

    start=introcs.rfind_str(json, '"dst":')
    result=(json[start+5:])
    value=(first_inside_quotes(result))
    return value


def has_error(json):
    """
Returns True if the response to a currency query encountered an error.

Given a JSON string provided by the web service, this function returns True if the
query failed and there is an error message. For example, if the json is
    
    '{"success":false,"src":"","dst":"","error":"Source currency code is invalid."}'

then this function returns True (It does NOT return the error message 
'Source currency code is invalid'). On the other hand if the json is 
    
    '{"success": true, "src": "2 United States Dollars", "dst": "1.772814 Euros", "error": ""}'

then this function returns False.

The web server does NOT specify the number of spaces after the colons. The JSON
    
    '{"success":true, "src":"2 United States Dollars", "dst":"1.772814 Euros", "error":""}'
    
is also valid (in addition to the examples above).

Parameter json: a json string to parse
Precondition: json a string provided by the web service (ONLY enforce the type)

    """
    
    assert type(json)==str, 'Not a string'
    
    start=introcs.rfind_str(json, '"error":')
    result=(json[start+7:])
    value=(first_inside_quotes(result))
    vlength=len(value)
    check = vlength >= 3
    
    return check 


def service_response(src, dst, amt):
    """
Returns a JSON string that is a response to a currency query.

A currency query converts amt money in currency src to the currency dst. The response 
should be a string of the form

    '{"success": true, "src": "<src-amount>", dst: "<dst-amount>", error: ""}'

where the values src-amount and dst-amount contain the value and name for the src 
and dst currencies, respectively. If the query is invalid, both src-amount and 
dst-amount will be empty, and the error message will not be empty.

There may or may not be spaces after the colon.  To test this function, you should
chose specific examples from your web browser.

Parameter src: the currency on hand
Precondition src is a nonempty string with only letters

Parameter dst: the currency to convert to
Precondition dst is a nonempty string with only letters

Parameter amt: amount of currency to convert
Precondition amt is a float or int

    """
    
    assert type(src)==str, 'Not a string'
    assert introcs.isalpha(src), 'This contains more than letters or is an empty string'
    
    assert type(dst)==str, 'Not a string'
    assert introcs.isalpha(dst), 'This contains more than letters or is an empty string'
    

    assert type(amt)!=str, 'Not an integer or a float'
    check1=introcs.isfloat(str(amt))
    check2=introcs.isint(str(amt))
    assert True == check1 or check2, 'Not an integer or a float'

    
    q = 'https://ecpyfac.ecornell.com/python/currency/fixed?src='
    r = src+'&dst='+dst+'&amt='+str(amt)+'&key='+APIKEY
    
    result=introcs.urlread(q+r)
    return result


def iscurrency(currency):
    """
Returns True if currency is a valid (3 letter code for a) currency.

It returns False otherwise.

Parameter currency: the currency code to verify
Precondition: currency is a nonempty string with only letters

    """
  
    webinquiry=(service_response(currency, currency, 2))

    start=introcs.find_str(webinquiry, ' ')
    end=introcs.find_str(webinquiry, ',')
    value=(webinquiry[start+1:end])
    size=(len(value))
    check = size == 4
    return check


def exchange(src, dst, amt):
    """
Returns the amount of currency received in the given exchange.

In this exchange, the user is changing amt money in currency src to the currency 
dst. The value returned represents the amount in currency currency_to.

The value returned has type float.

Parameter src: the currency on hand
Precondition src is a string for a valid currency code

Parameter dst: the currency to convert to
Precondition dst is a string for a valid currency code

Parameter amt: amount of currency to convert
Precondition amt is a float or int

    """
    
    validation1=(iscurrency(src))
    validation2=(iscurrency(dst))
    
    assert True == validation1 and validation2, 'Not a valid 3 Letter Currency Code.'
    
    assert type(amt)!=str, 'This is a string'
    check1=introcs.isfloat(str(amt))
    check2=introcs.isint(str(amt))
    assert True == check1 or check2, 'Not an integer or a float'
    
    q=(service_response(src, dst, amt))
    
    e=(get_dst(q))
    
    currency_to=(float(before_space(e)))

    return currency_to 
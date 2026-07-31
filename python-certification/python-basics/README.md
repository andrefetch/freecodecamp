# Chapter 1: Python Basics

Quick notes on what this chapter covers, plus the projects I built.

## Variables and data types

You don't declare a type, Python works it out from the value.

```python
name = 'Alice'      # str
age = 20            # int
score = 80.5        # float
is_student = True   # bool
```

`type(score)` tells you the exact type. `isinstance(score, float)` gives you a
True or False, which is nicer when you actually want to check something.

## Strings

Single or double quotes, doesn't matter. Join them with `+`, but numbers need
`str()` first, and `+=` tacks something onto the end.

```python
full_name = first_name + ' ' + last_name
info = full_name + ' is ' + str(age) + ' years old'
```

f-strings are much easier to read once there's more than one value:

```python
card = f'Employee: {full_name} | Age: {age} | Salary: ${salary}'
```

Indexing starts at 0. Slices `[start:end]` leave out the end index.

```python
code = 'DEV-2026-JD-001'
code[0:3]    # 'DEV'
code[4:8]    # '2026'
code[-1]     # '1'
```

## Numbers

`+ - * /` as usual, plus `//` for floor division, `%` for the remainder and
`**` for powers. `/` always gives you a float. `round(value, 2)` is what you
want for money, otherwise you get a pile of decimals.

## Booleans and conditionals

Comparisons (`==`, `!=`, `>`, `>=`) give back True or False. `if` / `elif` /
`else` picks the first branch that matches and skips the rest.

```python
if seat_type == 'Premium':
    service_charges = 5
elif seat_type == 'Gold':
    service_charges = 3
else:
    service_charges = 1
```

The indentation is what makes the block, there are no braces.

`and` needs both sides true, `or` needs one, `not` flips it. `and` binds tighter
than `or`, so brackets are worth adding when you mix them.

## Functions and scope

`def` makes a function, `return` sends a value back. No return means you get
`None`.

```python
def apply_discount(price, percent):
    return price - (price * percent / 100)
```

Parameters can have defaults, and you can pass arguments by name.

Variables made inside a function are local and disappear when it finishes. A
function can read a global variable, but assigning to that name just makes a new
local one instead of changing the global.

## Projects

Done:

| Project | What it covers |
| --- | --- |
| [Report Card Printer](build-a-report-card-printer/report_card_printer.py) | Variables, the four basic types, `type()` and `isinstance()` |
| [Employee Profile Generator](build-an-employee-profile-generator/employee_generator.py) | String joining, `str()`, f-strings, slicing an ID apart |
| [Bill Splitter](build-a-bill-splitter/bill_splitter.py) | Running totals, tip percentage, division, `round()` |
| [Movie Ticket Booking Calculator](build-a-movie-booking-calculator/movie_booking_calculator.py) | `if`/`elif`/`else`, `and`/`or`, nested conditions |

Still to do: Travel Weather Planner, Apply Discount Function, Caesar Cipher,
RPG Character, then the review and quiz.

## Running them

```bash
python build-a-bill-splitter/bill_splitter.py
```

Each one is a standalone script that just prints its output.

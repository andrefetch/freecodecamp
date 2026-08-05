# Chapter 1: Python Basics (Finished! -- In 2d)

I already know most of this, so I'm going back through it to make the
fundamentals solid instead of half remembered. These are the bits worth writing
down, not a full walkthrough of the syntax.

## What I'm covering

Variables, data types, strings, numbers, booleans and conditionals, functions
and scope.

## Things worth remembering

`type()` gives the exact type, `isinstance()` gives a True or False. Use the
second one when you're actually branching on something.

`+` only joins strings, so numbers need `str()` first. Past two values I should
just be using an f-string.

Slices leave out the end index, so `code[4:8]` is four characters, not five.

`/` always returns a float, even on whole numbers. Anything to do with money
gets a `round(value, 2)` at the end.

`and` binds tighter than `or`, so `a or b and c` is `a or (b and c)`. Brackets
whenever I mix them, no exceptions.

A function with no `return` hands back `None`.

Assigning to a name inside a function makes a new local variable, it doesn't
touch the global one with the same name. Pass things in, return things out.

`isinstance(True, int)` is True. Booleans are integers underneath, so a check
that lets an `int` through lets `True` through as well.

Check the arguments first and return early on each bad one. The real work then
sits at the bottom with nothing wrapped around it.

A default argument can turn two functions into one. `caesar(text, shift,
encrypt=True)` does both directions, and `encrypt` and `decrypt` are one-line
wrappers over it.

`alphabet[shift:] + alphabet[:shift]` rotates a string. A negative shift rotates
it the other way, which is the whole reason decrypting is just encrypting with
`-shift`.

`str.maketrans()` plus `.translate()` swaps every character in one pass, no loop
needed. Build the table from both cases at once and capitals come out right.

`'●' * 3` repeats a string. Multiply by the stat, pad the remainder with the
empty character, and you have a bar without touching a loop.

## Projects

Done:

| Project | Focus |
| --- | --- |
| [Report Card Printer](build-a-report-card-printer/report_card_printer.py) | Variables and the four basic types |
| [Employee Profile Generator](build-an-employee-profile-generator/employee_generator.py) | String joining, f-strings, slicing an ID apart |
| [Bill Splitter](build-a-bill-splitter/bill_splitter.py) | Running totals, tip percentage, rounding |
| [Movie Ticket Booking Calculator](build-a-movie-booking-calculator/movie_booking_calculator.py) | Conditionals and nested logic |
| [Travel Weather Planner](build-a-weather-planner/weather_planner.py) | Chained comparisons, `and`/`or`/`not` in one decision |
| [Apply Discount Function](apply-discount-function/apply_discount.py) | Validating arguments before doing the maths |
| [Caesar Cipher](caesar-cypher/caesar-cypher.py) | Default arguments, rotating a string, `translate()` |
| [RPG Character](build-a-rpg-character/rpg_character.py) | Guard clauses stacked up, string repetition for the stat bars |

## Running them

```bash
python build-a-bill-splitter/bill_splitter.py
```

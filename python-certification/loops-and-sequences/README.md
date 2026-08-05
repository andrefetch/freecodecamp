# Chapter 2: Loops and Sequences (Finished! -- In 3d)

One lecture, one workshop and one lab. Lists and tuples first, then loops, then
a pile of built-ins that mean you don't have to write the loop at all. Notes
below are just the stuff I want to actually stick.

## What I'm covering

Lists and list methods, tuples, `for` and `while` loops, `range()`,
`enumerate()` and `zip()`, list comprehensions, `filter()`, `map()`, `sum()`,
and lambdas.

## Things worth remembering

Lists change, tuples don't. If I'm not going to touch it again after building
it, make it a tuple. Python throws a `TypeError` the second I try to reassign
into one.

`append()` adds one thing. `extend()` adds each thing. So
`numbers.append([6, 8])` puts a list inside my list, which is basically never
what I wanted.

`sort()` sorts in place and gives back `None`. `sorted()` leaves the original
alone and gives back a new list. So if I write `x = numbers.sort()` I've just
set x to `None`. Easy one to get caught by.

`sorted()` takes `key=` and `reverse=`. `sorted(words, key=len)` sorts by length
and I don't have to write any comparison myself.

`del` and `pop()` want an index, `remove()` wants the actual value. Only `pop()`
gives the item back to me.

Slices take a step too. `numbers[1::2]` is every other one, and a negative step
walks it backwards.

`range(stop)` starts at 0 and stops before the number I gave it. So if I want 1
through n I have to write `range(1, n + 1)`, which is exactly what the pattern
generator needed.

`range()` only takes ints. Give it a float and it's a `TypeError`, it won't
round it for me.

`enumerate()` hands me the index and the value together so I never need to keep
a counter myself. That's the whole Pin Extractor really, the position of the
line is what decides which word gets measured.

`zip()` runs through two sequences side by side and just stops at the shorter
one. Nothing warns me if they're different lengths.

`.split()` with nothing in it splits on any whitespace and drops the empty bits.
`.split('\n')` keeps them. On a poem with a blank line those two give me
different answers.

Build up a list inside the loop and `' '.join()` it at the end instead of gluing
a string together with `+=` every pass.

Nested loops: the inner one runs all the way through for every single pass of
the outer one. Two lists of 4 is 16 goes, not 8.

Check the length before I reach for an index. `if len(words) > line_index`
first, then index. That's the difference between getting an answer and getting
an `IndexError`.

`break` gets out of the loop, `continue` just skips the rest of that one pass.
The `else` on a loop only runs if nothing broke out, so it's the "checked
everything, found nothing" branch.

A list comprehension is the loop and the condition on one line,
`[num for num in range(21) if num % 2 == 0]`. Once it needs more than one
expression and one condition it should go back to being a normal loop.

`filter()` and `map()` give back iterators, not lists, so they need `list()`
wrapped round them before I can print them or index into them.

A lambda is for the throwaway function I'd only be defining to pass it somewhere
anyway. If it deserves a name it deserves a `def`.

## Projects

Done:

| Project | Focus |
| --- | --- |
| [Pin Extractor](build-a-pin-extractor.py/pin_extractor.py) | Nested loops, `enumerate()`, pulling text apart, building up a result |
| [Number Pattern Generator](number-patter-generator/number_pattern_gen.py) | `range()`, checking the argument first, list then join |

## Running them

```bash
python number-patter-generator/number_pattern_gen.py
```

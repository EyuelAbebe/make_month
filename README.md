# make_month
==========

Given a year and month, it returns a month object, with method day. Given a day, the month object returns which day of the week the given day is.

It uses a variation of [Gauss Algorithm](http://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week#Formulas_derived_from_Gauss.27s_algorithm) to calculate the day of the week.

## Example

```bash
>>> from make_month import *
>>> this_july = make_month(2014, 7)
>>> this_july.day(12)
'Saturday'
>>> 
```

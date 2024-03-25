# Regex Autotagging Exercise 1 

## Special Reserve Characters

Find: `&` *found 315*

Replace with: `&amp;`

Find: `<` *didn't find any*

Find: `>` *didn't find any*

## Capturing Movie

Find: `.+` *found 25095*

Replace with: `<movie>\0</movie>`

## Capturing Movie Title


Find: `(<movie>)(.+?)\t`

Replace with: `\1<title>\2</title>`

## Capturing Year

Find: `(</title>)(\w{4})`

Replace with: `\1<year>\2</year>`


## Capturing Country

Find: `(</year>)\s+(.+?)\t`

Replace with: `\1<country>\2</country>`


## Capturing Runtime 

Find: `(</country>)(\d+)`

Replace with: `\1<runTime unit="min">\2</runTime>`

## Removing "Min"

Find: `<runTime unit="min">(\d+)<\/runTime> min<\/movie>`

Replace with: `<runTime unit="min">\1</runTime></movie>`


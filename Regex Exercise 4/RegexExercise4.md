
# Bojack


### Remove `<!doctype html>` and turn `<html>` into `<xml>`

Find: `(<!doctype html>\n*)?(</?)ht(ml>)`

Replace: `\2x\3`



### Capturing `<head>` and its contents to replace with just the `<title>`

Find: `<head>[\s\S]*?<title>([\s\S]*?)<\/title>[\s\S]*?<\/head>`

Replace: 
`<title>$1</title>`

### Getting rid of `<h4>`
Find: `<h4>.*?<\/h4>`

Replace: blank


### Getting rid of `<h1>`

Find: `<h1>.*?<\/h1>`

Replace: blank


### Getting rid of `<article>`

Find: `<article>` `</article>` 

Replace: blank

### Capturing brackets and their contents put them in `<action>`

Find: `\[(.+?)\]`

Replace: `<action>$1</action>`


### Capturing all the different variations of ♪ in `<i>`to replace `<i>` with `<song>`

Find: `<i>([^<]*[♪♪][^<]*)<\/i>`

Replace: `<song>$1</song>`

### Capturing `<p>` and the text inside to replace `<p>` with `<speech>`

Find:` <p>(.*?)</p>` *dot matches all*

Replace: `<speech speaker="Speaker">$1</speech>`



### Notes: 
 Some of the `<speech>` elements that were originally `<p>` aren't always correct because there are some instances in the files where `<p>` isnt speech and is just an action or music. However the majority does correctly reflect the `<speech>` element. 







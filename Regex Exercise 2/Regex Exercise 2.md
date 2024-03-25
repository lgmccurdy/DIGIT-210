## Regex Exercise 2

### Special Reserve Characters
Find: `&` *no results found*

Find: `<` *no results found*

Find: `>` *no results found* 



### Leading Space Characters
Find: `^ + `

Replace: ` `

### Lines
Find: `.+`

Replace with: `<line>\0</line>`


### Roman numerals 

Find: `<line>\s*([IVXLCDM]+)\s*<\/line>`

Replace with: `</sonnet>\n<sonnet number="\1">\n`

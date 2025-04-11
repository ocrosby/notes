# Learn lua

- Leanring basic lua is highly reocmmended when configuring the neovim config.
- It's a really simple & small language

## Lua

### Comments

```lua
-- comment
print("Hi") -- comment

--[[
 multi-line 
 comment
]]
```

### Variables

```lua
local x = 10 -- number
local name = "sid" -- string
local isAlive = true -- boolean
local a = nil --no value or invalid value

-- increment in numbers
local n = 1
n = n + 1
print(n) -- 2

-- strings
-- Concatenate strings
local phrase = "I am"
local name = "Sid"

print(phrase .. " " .. name) -- I am Sid
print("I am " .. "Sid")
```

### Comparison Operators

```lua
 == equal
 < less than
 > greater than
 <= less than or equal to
 >= greater than or equal to
 ~= not equal
```

### Conditional Statements

```lua
-- Number comparisons
local age = 10

if age > 18 then
  print("over 18") -- this will not be executed
end

-- elseif and else
age = 20

if age > 18 then
  print("over 18")
elseif age == 18 then
  print("18 huh")
else
  print("kiddo")
end

-- Boolean comparison
local isAlive = true

if isAlive then
    print("Be grateful!")
end

-- String comparisons
local name = "sid"

if name ~= "sid" then
  print("not sid")
end
```

### Combining Statements

```lua
local age = 22

if age == 10 and x > 0 then -- both should be true
  print("kiddo!")
elseif x == 18 or x > 18 then -- 1 or more are true
  print("over 18")
end

-- result: over 18
```

### Invert Value

```lua
local isAlive = true

if not isAlive then
  print(" ye ded!")
end
```

### Functions

```lua
local function print_num(a)
  print(a)
end

-- or

local print_num = function(a)
  print(a)
end

print_num(5) -- prints 5 

-- multiple parameters
function sum(a, b)
  return a + b
end
```

### Scope

```lua
function foo()
  local n = 10
end

print(n) -- nil , n isn't accessible outside foo()
```


### Loops

```lua
local i = 1

while i <= 3 do
   print("hi")
   i = i + 1
end

for i = 1, 3 do
   print("hi")
end
-- Both print "hi" 3 times
```

### Arrays

```lua
local colors = { "red", "green", "blue" }

print(colors[1]) -- red

-- Different ways to loop through lists
-- #colors is the length of the table, #tablename is the syntax

for i = 1, #colors do
  print(colors[i])
end

-- ipairs 
for index, value in ipairs(colors) do
   print(colors[index])
   -- or
   print(value)
end

-- If you dont use index or value here then you can replace it with _ 
for _, value in ipairs(colors) do
   print(value)
end
```

### Dictionaries

```lua
local info = { 
   name = "sid",
   age = 20,
   isAlive = true
}

-- both print sid
print(info["name"])
print(info.name)

-- Loop by pairs
for key, value in pairs(info) do
   print(key .. " " .. tostring(value))
end

-- prints name sid, age 20 etc
```

### Nested Tables

```lua
-- Nested lists
local data = {
    { "sid", 20 },
    { "tim", 90 },
}

for i = 1, #data do
  print(data[i][1] .. " is " .. data[i][2] .. " years old")
end

-- Nested dictionaries
local data = {
    sid = { age = 20 },
    tim = { age = 90 },
}
```

### Modules

Import code from other files

```lua
require("path")

-- for example in ~/.config/nvim/lua , all dirs and files are accessable via require
-- Do note that all files in that lua folder are in path!
-- ~/.config/nvim/lua/abc.lua 
-- ~/.config/nvim/lua/abc/init.lua

 require "abc"

-- both do the same thing
```

### vim.tbl_deep_extend

This is a newovim function which is used for merging tables and their values recursively. Most plugins use it for merging config tables.

```lua
-- table 1
local person = {
    name = "joe",
    age = 19,
    skills = {"python", "html"},
}

-- table 2
local someone = {
    name = "siduck",
    skills = {"js", "lua"},
}

-- "force" will overwrite equal values from the someone table over the person table
local result = vim.tbl_deep_extend("force", person, someone)

-- result : 
{
    name = "siduck",
    age = 19,
    skills = {"js", "lua"},
}

-- The list tables wont merge cuz they dont have keys 
```
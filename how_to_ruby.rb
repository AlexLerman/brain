### RUNNING THIS FILE
# $> ruby how_to_ruby.rb

### MESS AROUND WITH INTERPRETED RUBY
# $> irb

### COMMENTS

# comments are created with the # character.
# you can make block comments like this:

=begin
 block
 comment
=end

# but the =begin and =end can't be indented, so don't use this to comment out blocks of code.

### STRINGS

print("\n" + '### STRINGS' + "\n\n")

# There are many, many ways of creating a string literal in Ruby. The most
# common are single and double quotes.

# These actually behave slightly differently. Single quotes will encode the
# characters between them literally. Double quotes let you use escape characters.

print('single quotes \n')
print("\n double quotes \n")

# Double quotes also let you use string interpolation:

pet = 'ham'
print("double quotes: a wizard and his pet #{pet} \n")

# Single quotes don't do string interpolation.
# You can use `puts` instead of `print` to automatically add a line break at the
# end of your printed string.

puts('single quotes: a wizard and his pet #{pet}')

### METHODS

def p(obj)
  string = obj.to_s()
  print(string + "\n")
end

p("\n### METHODS\n")

# Method names can end in a question mark or exclamation point.
# these are conventionally used for boolean methods and destructive methods, respectively.

p("a string".is_a?(String)) # prints `true`

s = "chunky bacon"
s.capitalize!
p(s) # prints `CHUNKY BACON`

# You can define (and call) methods without using argument parentheses:

def print_title string
  p "\n" + string
end

def pretty_print hash, indent_spaces = 2, indent_level = 0
  current_indent = indent_spaces * indent_level
  hash.each_pair do |key, value|
    print " " * current_indent
    print key.inspect
    print " => "
    
    if value.is_a? Hash # same as `value.is_a?(Hash)`
      print "\n"
      pretty_print value, indent_spaces, indent_level + 1
    else
      p value.inspect
    end
  end
end

### HASHES AND ARRAYS

pretty_print({:foo => {:bar => 'ziff'}, 'kludge' => 3, 4 => 5})


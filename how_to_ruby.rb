### RUNNING THIS FILE
# $> ruby how_to_ruby.rb

### COMMENTS

# comments are created with the # character.
# you can make block comments like this:

=begin
 block
 comment
=end

# but the =begin and =end can't be indented, so don't use this to comment out blocks of code.

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


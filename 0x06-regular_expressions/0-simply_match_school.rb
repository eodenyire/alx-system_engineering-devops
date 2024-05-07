#!/usr/bin/env ruby
# Script to match the string "School" using a regular expression

# Check if the argument contains the exact string "School"
if ARGV[0] =~ /School/
  puts ARGV[0]
else
  puts ""
end

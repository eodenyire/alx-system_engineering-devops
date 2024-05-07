#!/usr/bin/env ruby

# Script to match a specific pattern using a regular expression

# Check if the argument matches the specified pattern
if ARGV[0] =~ /hbt{2,5}n/
  puts ARGV[0]
else
  puts ""
end

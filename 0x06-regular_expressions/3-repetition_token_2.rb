#!/usr/bin/env ruby
#+ Using the project instructions, create a Ruby script that accepts
#+ one argument and pass it to a regular expression matching method

def match_hbtn(argument)
  pattern = /(hbt+n)/
  match = argument.scan(pattern)
  if match.any?
    puts match.join
  else
    puts ""
  end
end

if ARGV.length < 1
  puts "Please provide an argument."
else
  argument = ARGV[0]
  match_hbtn(argument)
end

#!/usr/bin/env ruby
#+ Using the project instructions, create a Ruby script that accepts
#+ one argument and pass it to a regular expression matching method

def match_10_dig_no(argument)
  pattern = /^\d{10}$/
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
  match_10_dig_no(argument)
end

#!/usr/bin/env ruby
# A script to output: [SENDER],[RECEIVER],[FLAGS]
#+ The sender phone number or name (including country code if present)
#+ The receiver phone number or name (including country code if present)
#+ The flags that were use

if ARGV.length < 1
  puts "Usage: #{$0} <logfile>"
  exit(1)
end

logfile = ARGV[0]

results = []

File.readlines(logfile).each do |line|
  if line =~ /Receive SMS|Sent SMS/
    sender =  line.match(/\[from:(.*?)\]/)
    receiver = line.match(/\[to:(.*?)\]/)
    flags = line.match(/\[flags:(.*?)\]/)

    if sender && receiver && flags
      results << "#{sender[1]},#{receiver[1]},#{flags[1]}"
    end
  end
end

puts results

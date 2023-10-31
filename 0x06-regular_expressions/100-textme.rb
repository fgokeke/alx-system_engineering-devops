#!/usr/bin/env ruby
# A script to output: [SENDER],[RECEIVER],[FLAGS]
#+ The sender phone number or name (including country code if present)
#+ The receiver phone number or name (including country code if present)
#+ The flags that were use

puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")

#!/usr/bin/env ruby

input = ARGV[0]

matches = input.scan(/^hb(t+)n$/)

if matches.empty?
  puts "No match"
else
  puts matches.join(" ")
end

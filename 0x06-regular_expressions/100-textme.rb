#!/usr/bin/env ruby
arg = ARGV[0]
sender = arg.scan(/\[from:([^\]]+)\]/).join
receiver = arg.scan(/\[to:([^\]]+)\]/).join
flags = arg.scan(/\[flags:([^\]]+)\]/).join
puts "#{sender},#{receiver},#{flags}"

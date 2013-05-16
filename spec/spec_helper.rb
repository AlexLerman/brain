require 'spork'
require 'rspec'

### App
require './lib/neuron'

Spork.prefork do
  # this block will run when Spork starts up

  ### Libraries
  require 'active_support/core_ext'  
end

Spork.each_run do
  # no-op for now
  # this block will run before each test run
end

require 'spec_helper'

describe 'a new Neuron' do
  subject { Neuron.new }
  
  it { should be_a Neuron }
  its(:activation) { should eq 0 }
end
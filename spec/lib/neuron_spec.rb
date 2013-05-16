require 'spec_helper'

describe Neuron do
  let(:neuron) { Neuron.new }

  context '#new' do
    subject { neuron }
    
    it { should be_a Neuron }
    its(:activation) { should eq 0 }
  end

  context '#activation' do
    subject { neuron.activation } 
    let(:neuron) { Neuron.new(:input_neurons => input_neurons) }

    context 'with no input neurons' do
      let(:input_neurons) { [] }

      it { should eq 0 }
    end

    context 'with input neurons' do
      let(:input_neurons) do
        [ mock('input neuron', :activation => 1),
          mock('input neuron', :activation => 2),
          mock('input neuron', :activation => 3),
        ]
      end

      it { should eq 6 }
    end
  end
end
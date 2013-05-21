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
    let(:neuron) { Neuron.new(:input_synapses => input_synapses) }

    context 'with no input neurons' do
      let(:input_synapses) { [] }

      it { should eq 0 }
    end

    context 'with input neurons' do
      let(:input_synapses) do
        [ Synapse.new(mock('input neuron', :activation => 1), weight=1),
          Synapse.new(mock('input neuron', :activation => 2), weight=2),
          Synapse.new(mock('input neuron', :activation => 3), weight=3),
        ]
      end

      it { should eq 1 + 4 + 9 }
    end
  end
  
  context '#connect' do
    let(:input_neurons) do
      [mock('input neuron', :activation => 1), mock('input neuron', :activation => 2)]
    end
    
    it 'connects the given neuron to this one as an input' do
      neuron.connect input_neurons.first, 1
      neuron.activation.should eq 1
    end
    
    it 'randomly assigns the weight if none is given' do
      Neuron.any_instance.stub(:rand).and_return(0, 1)
      neuron.connect input_neurons.first
      neuron.connect input_neurons.last
      neuron.activation.should eq(0.4 * 1.0 + 0.6 * 2.0)
    end
  end
  
  context '#learn!' do
    let(:input_neurons) do
      [mock('input neuron', :activation => 1), mock('input neuron', :activation => -2)]
    end
    
    it 'adjusts the weights of the input synapses' do
      neuron.connect input_neurons.first, 1
      neuron.connect input_neurons.last, 1
      neuron.activation.should eq(-1)
      
      neuron.learn!
      neuron.clear_activation
      neuron.activation.should be_within(0.0001).of(-1.2)
    end
  end
end
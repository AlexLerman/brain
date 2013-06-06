class Synapse
  attr_accessor :input_neuron
  attr_accessor :weight
  
  def initialize input_neuron, weight
    super
    self.input_neuron = input_neuron
    self.weight = weight
  end
  
  def activation
    input_neuron.activation
  end
end

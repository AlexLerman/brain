class Neuron
  def initialize(options={})
    @input_neurons = []
    add_input(options[:input_neurons]) if options[:input_neurons]
  end
  
  def add_input(*input_neurons)
    @input_neurons.concat(input_neurons).uniq!
  end
  
  def activation
    ease(@input_neurons.sum(&:activation).to_f) #TODO: implement Array#sum
  end
  
  def ease(x)
    x
  end
  
  alias_method :add_inputs, :add_input
end
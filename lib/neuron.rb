class Neuron
  LEARNING_CONSTANT = 0.05
  
  def initialize(options={})
    @input_synapses = []
    add_input(*options[:input_synapses]) if options[:input_synapses].is_a? Array
  end
  
  def add_input(*input_synapses)
    @input_synapses.concat(input_synapses).uniq! { |s| s.input_neuron }
  end
  
  def activation
    @activation ||= ease(@input_synapses.sum(&:activation).to_f)
  end
  
  def connect src, weight=nil
    if weight.nil?
      weight = rand * 0.2 + 0.4
    end
    synapse = Synapse.new(src, weight)
    self.add_input synapse
  end
  
  def learn!
    @input_synapses.each do |synapse|
      # Hebbian learning with Oja's rule to keep weights normalized
      synapse.weight += LEARNING_CONSTANT * activation * (synapse.activation - synapse.weight * activation)
    end
  end
  
  def clear_activation
    @activation = nil
  end
  
  def ease(x)
    x
  end
  
  alias_method :add_inputs, :add_input
end
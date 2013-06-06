require '~/Desktop/projects/brain/lib/neuron'
require '~/Desktop/projects/brain/lib/neuron/random_sigmoid_neuron'

$layers =0

class Brain
  DEFAULT_NEURONS_PER_LAYER = 32
  DEFAULT_NUMBER_OF_LAYERS = 4
  DEFAULT_NUMBER_OF_INPUT_NEURONS = 10
  
  attr_accessor :neurons
  attr_accessor :input_neurons
  attr_accessor :neuron_class

  def initialize options={}
    ret = super
    layers = options[:layers] || DEFAULT_NUMBER_OF_LAYERS
    neurons_per_layer = options[:neurons_per_layer] || DEFAULT_NEURONS_PER_LAYER
    input_neurons = options[:input_neurons] || DEFAULT_NUMBER_OF_INPUT_NEURONS
    self.neuron_class = options[:neuron_class] || RandomSigmoidNeuron
    
    create_and_connect_neurons layers, neurons_per_layer, input_neurons
    ret
  end
  
  def create_and_connect_neurons number_of_layers, neurons_per_layer, number_of_input_neurons
    layers = []
    layers << create_layer(number_of_input_neurons)
    number_of_layers.times do
      layers << create_layer(neurons_per_layer / (2 ** (layers.length - 1)), layers.last)
    end
    
    self.input_neurons = layers.first
    self.neurons = layers.flatten
    nil
  end
  
  def create_layer(number_of_neurons, layer_below=[])
    layer = []
    number_of_neurons.to_i.times do
      layer << (n = self.neuron_class.new)
      layer_below.each do |neuron_below|
        n.connect neuron_below
      end
    end
    puts "created layer #{$layers += 1}"
    layer
  end
  
  def train(inputs)
    input_neurons.each_with_index do |input, i|
      input.activation = inputs[i]
    end
    
    neurons.each_with_index do |n, i|
      n.activation
      puts "neuron #{i.to_s.ljust(4)} : #{n.activation} #{n.input_synapses.map { |s| s.weight.round(2) }.join(", ")}"
    end
    
    neurons.each do |n|
      n.learn!
    end
    
    neurons.each do |n|
      n.clear_activation
    end
  end
  
  def to_s
    "#<yo dawg i'm a brain>"
  end
  
  def inspect
    "#<yo dawg i'm a brain>"
  end
end

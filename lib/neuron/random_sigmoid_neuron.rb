class RandomSigmoidNeuron < Neuron
  def ease x
    v = sigmoid(x + bias)
    return 1 if (rand) < v
    return 0
  end
  
  def bias
    -input_synapses.sum(&:weight) / 2.0
  end
  
  def sum_weight
    input_synapses.sum(&:weight)
  end
  
  def sigmoid z
    1 / (1 + Math::E ** -z)
  end
  
  def learn!
    @input_synapses.each do |synapse|
      unless synapse.activation == 0 && self.activation == 0
        if (synapse.activation > 0) == (self.activation > 0)
          synapse.weight += 0.05
        else
          synapse.weight -= 0.05
        end
      end
      if synapse.weight < 0
        synapse.weight = 0
      end
    end
  end
end

'''

Sefika Efeoglu  sefeoglu@gmail.com
'''

from gym import spaces
import numpy as np
from pgmpy.factors.discrete import DiscreteFactor
from pgmpy.sampling import GibbsSampling
from pgmpy.models import MarkovModel


class BoxExtended(spaces.Box):
    def sample(self, sampling="Random"):

      if sampling == "Random":
        self.random_sampling()
      elif sampling == "Gibbs":
        self.gibbs_sampling()
      elif sampling == "Logic":
        self.logic_sampling()
      elif sampling == "Importance":
        self.importance_sampling()
        
      
    def gibbs_sampling(self):
      '''
      Improve gibbs sampling Algorithm
      '''
      pass
    def logic_sampling(self):
      '''
      Logic Sampling
      '''
      pass
    def importance_sampling(self):
      '''
        Importance Sampling
      '''
      pass
    def random_sampling(self):
      '''
      Random Sampling
      '''
      pass
if __name__ == "__main__":
  model = MarkovModel([('A', 'B'), ('C', 'B')])
  factor_ab = DiscreteFactor(['A', 'B'], [2, 2], [1, 2, 3, 4])
  factor_cb = DiscreteFactor(['C', 'B'], [2, 2], [5, 6, 7, 8])
  model.add_factors(factor_ab, factor_cb)
  gibbs = GibbsSampling(model)
  gen = gibbs.generate_sample(size=2)
  for sample in gen:
    print(sample)
'''
Defines a class, Neuron473862845, of neurons from Allen Brain Institute's model 473862845

A demo is available by running:

    python -i mosinit.py
'''
class Neuron473862845:
    def __init__(self, name="Neuron473862845", x=0, y=0, z=0):
        '''Instantiate Neuron473862845.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron473862845_instance is used instead
        '''
               
        self._name = name
        # load the morphology
        from load_swc import load_swc
        load_swc('Scnn1a-Tg3-Cre_Ai14_IVSCC_-168093.03.01.01_328874467_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon
 
        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron473862845_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im', u'K_P', u'K_T', u'Kv3_1', u'NaTs', u'Nap', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 128.36
            sec.e_pas = -87.2847976685
        for sec in self.apic:
            sec.cm = 2.36
            sec.g_pas = 0.000577254971551
        for sec in self.axon:
            sec.cm = 1.0
            sec.g_pas = 0.000240001967843
        for sec in self.dend:
            sec.cm = 2.36
            sec.g_pas = 1.18711074921e-05
        for sec in self.soma:
            sec.cm = 1.0
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Im = 0.0011055
            sec.gbar_Ih = 0
            sec.gbar_NaTs = 0.15772
            sec.gbar_Nap = 0.00141589
            sec.gbar_K_P = 0.0199943
            sec.gbar_K_T = 0.00017238
            sec.gbar_SK = 0.00255583
            sec.gbar_Kv3_1 = 0.184452
            sec.gbar_Ca_HVA = 0.000975548
            sec.gbar_Ca_LVA = 0.003055
            sec.gamma_CaDynamics = 0.000297953
            sec.decay_CaDynamics = 322.832
            sec.g_pas = 8.7571e-05
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)


import math

class MartensiteStart:
    def __init__(self, **kwargs):
        self.C = kwargs.get('C',0.0)
        self.N = kwargs.get('N',0.0)		
        self.Mn = kwargs.get('Mn',0.0)
        self.Si = kwargs.get('Si',0.0)
        self.Cr = kwargs.get('Cr',0.0)
        self.Mo = kwargs.get('Mo',0.0)
        self.Ni = kwargs.get('Ni',0.0)
        self.Al = kwargs.get('Al',0.0)
        self.Co = kwargs.get('Co',0.0)
        self.V = kwargs.get('V',0.0)
        self.W = kwargs.get('W',0.0)
        self.Nb = kwargs.get('Nb',0.0)
        self.Ta = kwargs.get('Ta',0.0)
        self.Zr = kwargs.get('Zr',0.0)
        self.Hf = kwargs.get('Hf',0.0)
        self.Cu = kwargs.get('Cu',0.0)	
        self.Ti = kwargs.get('Ti',0.0)		
        self.B = kwargs.get('B',0.0)	
        self.GZ = kwargs.get('grainsize',20.0)
        self.T = {}
        self.update_dependent_parameters()
        self.compute()

    def update_dependent_parameters(self):
        self.CSi = math.sqrt(self.C*self.Si)
        self.CMn = math.sqrt(self.C*self.Mn)
        self.CCr = math.sqrt(self.C*self.Cr)
        self.CMo = math.sqrt(self.C*self.Mo)
        self.SiMn = math.sqrt(self.Si*self.Mn)
        self.SiCr = math.sqrt(self.Si*self.Cr)
        self.SiMo = math.sqrt(self.Si*self.Mo)
        self.MnCr = math.sqrt(self.Mn*self.Cr)
        self.MnMo = math.sqrt(self.Mo*self.Mn)
        self.CrMo = math.sqrt(self.Cr*self.Mo)

        # Berechnung Wurzel-Parameter nach Dai und Yuan
        self.DaiYuan = math.sqrt((self.Ni+self.Mn)*(self.Cr+self.Mo+self.Al+self.Si))
            
        # Berechnung Wurzel-Parameter bei Kaar
        self.WurCN = math.sqrt(self.C + 0.86*self.N)
            
        # Berechnung ln für KG-Einfluss bei Lee
        self.KG = 11.64*math.log(self.GZ)	

    def compute(self):
        self.T['Payson & Savage']= round(((930 - 570*self.C - 60*self.Mn - 20*self.Si - 50*self.Cr - 20*self.Mo - 30*self.Ni)-32)*5/9) #Payson & Savage
        self.T['Kung & Rayment (mod. Payson)']= round(((930 - 570*self.C - 60*self.Mn - 20*self.Si - 50*self.Cr - 20*self.Mo - 30*self.Ni)-32)*5/9 + 10*self.Co) # Kung & Rayment (mod. Payson)	
        self.T['Rowland & Lyle']= round(((930 - 600*self.C - 60*self.Mn - 20*self.Si - 50*self.Cr - 20*self.Mo - 30*self.Ni)-32)*5/9) #Rowland & Lyle
        self.T['Kung & Rayment (mod. Rowland)']= round(((930 - 600*self.C - 60*self.Mn - 20*self.Si - 50*self.Cr - 20*self.Mo - 30*self.Ni)-32)*5/9 + 10*self.Co) #Kung & Rayment (mod. Rowland)
        self.T['Grange']= round(((1000 - 650*self.C - 70*self.Mn - 70*self.Cr - 50*self.Mo - 35*self.Ni)-32)*5/9)  #Grange
        self.T['Kung & Rayment (mod. Grange)']= round(((1000 - 650*self.C - 70*self.Mn - 70*self.Cr - 50*self.Mo - 35*self.Ni)-32)*5/9 + 10*self.Co)  #Kung & Rayment (mod. Grange)
        self.T['Nehrenberg']= round(((930 - 540*self.C - 60*self.Mn - 20*self.Si - 40*self.Cr - 20*self.Mo - 30*self.Ni)-32)*5/9)   #Nehrenberg
        self.T['Kung & Rayment (mod. Nehrenberg)']= round(((930 - 540*self.C - 60*self.Mn - 20*self.Si - 40*self.Cr - 20*self.Mo - 30*self.Ni)-32)*5/9 + 10*self.Co)   #Kung & Rayment (mod. Nehrenberg)
        self.T['Eichelmann']= round(1350 - 1665*(self.C+self.N) - 33*self.Mn - 28*self.Si - 42*self.Cr - 0*self.Mo - 61*self.Ni - 0*self.Al + 0*self.Co) #Eichelmann
        self.T['Steven & Haynes']= round(561 - 474*self.C - 33*self.Mn - 17*self.Cr - 21*self.Mo - 17*self.Ni)  #Steven & Haynes
        self.T['Kung & Rayment (mod. Steven & Haynes)']= round(561 - 474*self.C - 33*self.Mn - 17*self.Cr - 21*self.Mo - 17*self.Ni + 10*self.Co - 7.5*self.Si)  #Kung & Rayment (mod. Steven & Haynes)
        self.T['Andrews lin.']= round(539 - 423*self.C - 30.4*self.Mn - 12.1*self.Cr - 7.5*self.Mo - 17.7*self.Ni)  #Andrews lin.
        self.T['Kung & Rayment (mod. Andrews lin.)	']= round(539 - 423*self.C - 30.4*self.Mn - 12.1*self.Cr - 7.5*self.Mo - 17.7*self.Ni -7.5*self.Si + 10*self.Co)  #Kung & Rayment (mod. Andrews lin.)	
        self.T['Anrews parabol.']= round(512 - 453*self.C - 16.9*self.Ni + 15*self.Cr - 9.5*self.Mo + 217*self.C*self.C - 71.5*self.Mn*self.C - 67.6*self.Cr*self.C)  #Anrews parabol.   
        self.T['Kung & Rayment (mod. Anrews parabol.)	']= round(512 - 453*self.C - 16.9*self.Ni + 15*self.Cr - 9.5*self.Mo + 217*self.C*self.C - 71.5*self.Mn*self.C - 67.6*self.Cr*self.C + 10*self.Co - 7.5*self.Si)  #Kung & Rayment (mod. Anrews parabol.)	
        self.T['Tamura']= round(550 - 361*self.C - 39*self.Mn - 20*self.Cr - 5*self.Mo - 17*self.Ni - 30*self.Al + 15*self.Co - 10*self.Cu - 17*self.Ni - 35*self.V) #Tamura
        self.T['Steim']= round(550 - 350*self.C - 40*self.Mn - 5*self.Si - 20*self.Cr - 10*self.Mo - 17*self.Ni - 0*self.Al + 0*self.Co) #Steim
        self.T['Monma']= round(550 - 350*self.C - 40*self.Mn - 0*self.Si - 20*self.Cr - 10*self.Mo - 17*self.Ni + 0*self.Al + 15*self.Co - 10*self.W - 10*self.Cu - 35*self.V) #Monma
        self.T['Eldis']= round(531 - 391.2*self.C - 43.3*self.Mn - 0*self.Si - 16.2*self.Cr - 0*self.Mo - 21.8*self.Ni - 0*self.Al + 0*self.Co) # Eldis
        self.T['Bott & Pickering']= round(502 - 810*self.C -1230*self.N - 13*self.Mn - 0*self.Si - 12*self.Cr - 54*self.Cu - 46*self.Mo - 30*self.Ni - 0*self.Al + 0*self.Co) # Bott & Pickering
        self.T['Kulmburg']= round(492 - 125*self.C - 65.5*self.Mn - 0*self.Si - 10*self.Cr - 0*self.Mo - 29*self.Ni - 0*self.Al + 0*self.Co)  # Kulmburg                   
        self.T['Ishida']= round(545 - 330*self.C - 23*self.Mn - 7*self.Si - 14*self.Cr - 5*self.Mo - 13*self.Ni + 2*self.Al + 7*self.Co -13*self.Cu - 4*self.Nb + 3*self.Ti +4*self.V) # Ishida
        # self['Finkler & Schirra'].T= round(635 - 474*self.C + 407.6*self.N - 61.1*(Nb+Zr) - 31.3*(Ta + Hf) - 33*self.Mn - 0*self.Si - 17*self.Cr - 21*self.Mo - 17*self.Ni + 0*self.Al + 0*self.Co - 39*self.V -11*self.W) # Finkler & Schirra
        self.T['Sverdlin & Ness']= round(520 - 320*self.C - 50*self.Mn - 5*self.Si - 30*self.Cr - 20*self.Mo - 20*self.Ni + 0*self.Al + 0*self.Co - 5*self.Cu) # Sverdlin & Ness
        self.T['Wang I']= round(545 - 470*self.C - 37.7*self.Mn - 3.96*self.Si - 21.5*self.Cr - 38.9*self.Mo - 0*self.Ni + 0*self.Al + 0*self.Co) # Wang I (lin)
        self.T['Wang II']= round(540 - 584.9*self.C - 117.7*self.Mn - 23.1*self.Si - 42.5*self.Cr + 49.9*self.Mo - 62.5*self.CSi + 178.3*self.CMn - 10*self.CCr + 52.5*self.CMo + 117.2*self.SiMn + 50.9*self.SiCr - 142.2*self.SiMo - 29.2*self.MnCr -9.7*self.MnMo + 69.9*self.CrMo) #Wang II - mit Wechselwirkungen
        self.T['Kunitake']= round(560.5 - 407.3*self.C - 37.8*self.Mn - 7.3*self.Si - 14.8*self.Cr - 4.5*self.Mo - 19.5*self.Ni + 0*self.Al + 0*self.Co -20.5*self.Cu) #Kunitake
        self.T['Liu']= round(550 - 361*self.C - 39*self.Mn - 0*self.Si - 20*self.Cr - 5*self.Mo - 17*self.Ni + 30*self.Al + 16*self.Co -35*self.V - 10*self.Cu - 5*self.W) #Liu 
        self.T['Capdevilla']= round((764.2 - 302.6*self.C - 30.6*self.Mn - 14.5*self.Si - 8.9*self.Cr + 2.4*self.Mo - 16.6*self.Ni + 0*self.Al + 8.58*self.Co)-273,15) #Capdevilla
        self.T['Mahieu']= round(539 - 423*self.C - 30.4*self.Mn - 7.5*self.Si - 0*self.Cr - 0*self.Mo - 0*self.Ni + 30*self.Al + 0*self.Co) # Mahieu
        self.T['Dai']= round(1184.15 - 199.8*self.C - 199.8*1.4*self.N - 21.7*self.Mn - 45*self.Si - 6.8*self.Cr - 55.9*self.Mo - 17.9*self.Ni + 0*self.Al - 1.9*(self.C+1.4*self.N)*(self.Mo+self.Cr+self.Mn) - 14.4*self.DaiYuan - 410 - 273,15)   #Dai   
        self.T['Kaar']= round(692 - 502*self.WurCN - 37*self.Mn - 14*self.Si + 20*self.Al - 11*self.Cr) # Kaar	
        self.T['Mikula']= round(635 - 549.8*self.C - 85.4*self.Mn - 69*self.Si - 18.1*self.Cr - 69.3*self.Mo - 31*self.Ni - 1746.5*self.B) # Mikula
        self.T['von Bohemen']= round(565 - 600*(1-math.exp(-0.96*self.C)) - 31*self.Mn - 13*self.Si - 10*self.Cr - 12*self.Mo - 18*self.Ni) #von Bohemen
        self.T['Lee & Park']= round(475.9 - 335.1*self.C - 34.5*self.Mn - 1.3*self.Si - 13.1*self.Cr - 10.7*self.Mo - 15.5*self.Ni - 9.6*self.Cu + self.KG) # Lee & Park
        self.T['Trzaska']= round(541 - 401*self.C - 36*self.Mn - 10.5*self.Si - 14*self.Cr - 17*self.Mo - 18*self.Ni) # Trzaska
        self.T['Gramlich']= round(517 - 423*self.C - 30.4*self.Mn + 82*self.Mo - 0*self.Ni + 37*self.Al -700*self.B) # Gramlich
        self.T['Ingber']= round(530.2 - 290.3*self.C - 35.5*self.Mn - 6.8*self.Si - 17.2*self.Ni - 20.8*self.Cr - 10.4*self.Mo + 7.1*self.Al + 4.8*self.Co - 75*(1-math.exp(-0.96*self.C))) # Ingber
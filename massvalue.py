#!/usr/bin/env python3
'''
  Mass value calculator

  Created by Peter Hague 2020
'''

import numpy as np

_KCONST = (4*np.pi)**(1/3) * (1/3)**(-2/3)


def getK(thickness, fueldensity, tankdensity):
    '''
      Returns the constant K
      This is the the tank mass divided by the fuel mass raised
      to the power (2/3). Dry mass is then ~kM^(2/3)
    '''
    return _KCONST * thickness * tankdensity * fueldensity**(-2/3)


def getParams(isp, k):
    '''
      Returns a dict of the two parameters required for
      mass value calculation

      isp - the specific impulse of the basic method
      k -
    '''
    return {"isp": isp, "k": k}


def basicMethodV1Params():
    '''
      Returns the default parameters for mass value calculation
    '''
    return getParams(300, getK(0.02, 1000, 3000))


def massValueApprox(payload, deltav, params):
    '''
      Calculate mass value using the Taylor series approximation
      payload - mass of payload in kg
      deltav - deltav in metres per second
    '''
    factor = deltav/(params["isp"]*9.81)
    M0 = payload*np.exp(factor - 1)
    Mdry = M0 + np.exp(factor)*params["k"]*M0**(2/3)
    return Mdry + payload


def transferOrbit(mu, rstart, rend):
    '''
      Works out the total delta-v of a minimum energy
      Hohmann transfer orbit between 2 circular orbits
      mu - gravitational parameter of central body
      rstart - start radius
      rend - end radius
    '''


if __name__ == "__main__":
    p = basicMethodV1Params()
    print("Mass value calculator\n")
    payload = float(input("Enter payload mass (kg):"))
    deltav = float(input("Enter delta-v (m/s):"))
    print("Mass value: {}".format(massValueApprox(payload, deltav, p)))

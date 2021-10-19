from math import log10

def R_A(S_V, S_C, R_V, R_C, S):
  numero = S_V * 10 ** (-R_V / 10)
  numero += S_C * 10 ** (-R_C / 10)
  numero /= S
  
  return -10 * log10(numero)
  
def R_A1(S_V, S_C, R_V, R_C):
  S = S_V + S_C
  return R_A(S_V, S_C, R_V, R_C, S)
  
#PROBADOR
S_V, S_C, R_V, R_C = float(input("S_V (m^2) = ")),\
float(input("S_C (m^2) = ")), float(input("R_V (dBA) = ")),\
float(input("R_C (dBA) = ")) # 1.5, 0.2, 35, 36

print("R_A =", round(R_A1(S_V, S_C, R_V, R_C), 2), "dBA")

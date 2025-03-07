import math

# ------------------------------------------------------------------------
def delta(valorA, valorB, valorC):
   if not isinstance(valorA, (int, float)) or not isinstance(valorB, (int, float)) or not isinstance(valorC, (int, float)):
      return None
   
   if valorA == 0:
      return None

   valorDelta = valorB**2 - 4*valorA*valorC
   
   return valorDelta


# ------------------------------------------------------------------------
def raizesEq2Grau(valorA, valorB, valorDelta):
   if not isinstance(valorA, (int, float)) or not isinstance(valorB, (int, float)) or not isinstance(valorDelta, (int, float)):
      return None
   
   if valorA == 0:
      return None

   if valorDelta < 0:
      return None

   raiz1 = (-valorB + math.sqrt(valorDelta))/(2*valorA)
   raiz2 = raiz1

   if valorDelta > 0:
      raiz2 = (-valorB - math.sqrt(valorDelta))/(2*valorA)
   
   return raiz1, raiz2
import math

# ------------------------------------------------------------------------
def delta(valorA, valorB, valorC):
   if not isinstance(valorA, (int, float)) or not isinstance(valorB, (int, float)) or not isinstance(valorC, (int, float)):
      return False, 'Os valores informados não são numéricos'
   
   if valorA == 0:
      return False, 'O valor de A não pode ser zero'

   valorDelta = valorB**2 - 4*valorA*valorC
   
   return True, valorDelta


# ------------------------------------------------------------------------
def raizesEq2Grau(valorA, valorB, valorDelta):
   if not isinstance(valorA, (int, float)) or not isinstance(valorB, (int, float)) or not isinstance(valorDelta, (int, float)):
      return False, 'Os valores informados não são numéricos'
   
   if valorA == 0:
      return False, 'O valor de A não pode ser zero'

   if valorDelta < 0:
      return False, 'O valor de delta não pode ser negativo'

   raiz1 = (-valorB + math.sqrt(valorDelta))/(2*valorA)
   raiz2 = raiz1

   if valorDelta > 0:
      raiz2 = (-valorB - math.sqrt(valorDelta))/(2*valorA)
   
   return True, raiz1, raiz2
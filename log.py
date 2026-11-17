import math


def logarithm(numero: float, base: float = math.e) -> float:
	"""Compute the logarithm of `numero` in the given base, without using math.log.

	Idea: any value can be written as  m * 2**e  with m between 1 and 2, so
	ln(value) = ln(m) + e * ln(2). Both ln(m) and ln(2) are computed with the series
	ln(x) = 2 * (z + z^3/3 + z^5/5 + ...),  where z = (x - 1) / (x + 1).
	"""
	numero = float(numero)
	base = float(base)
	if numero <= 0 or base <= 0 or base == 1:
		raise ValueError("El número y la base deben ser positivos y la base no puede ser 1.")

	# Step 1: decompose the number and the base as m * 2**e, with m in [1, 2).
	exponentes: list[int] = []
	valores_z: list[float] = [1.0 / 3.0]  # the first z is used to compute ln(2): (2-1)/(2+1) = 1/3
	for valor in (numero, base):
		mantisa, exponente = math.frexp(valor)  # valor = mantisa * 2**exponente, mantisa in [0.5, 1)
		mantisa *= 2.0                          # now mantisa is in [1, 2)
		exponentes.append(exponente - 1)
		valores_z.append((mantisa - 1.0) / (mantisa + 1.0))

	# Step 2: compute 2 * (z + z^3/3 + z^5/5 + ...) for each z.
	resultados: list[float] = []
	for z in valores_z:
		potencia: float = z      # z, z^3, z^5, ...
		denominador: int = 1     # 1, 3, 5, ...
		suma: float = 0.0
		while abs(potencia / denominador) >= 1e-16:
			suma += potencia / denominador
			potencia *= z * z
			denominador += 2
		resultados.append(2.0 * suma)

	# Step 3: ln(value) = ln(m) + e * ln(2), and the log in base b is ln(number) / ln(base).
	ln_dos, ln_mantisa_numero, ln_mantisa_base = resultados
	ln_numero = ln_mantisa_numero + exponentes[0] * ln_dos
	ln_base = ln_mantisa_base + exponentes[1] * ln_dos

	return ln_numero / ln_base

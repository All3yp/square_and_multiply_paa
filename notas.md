---
marp: true
theme: default
class: invert
---

## Ideia do algoritmo

```text
b^n = b^(n/2) × b^(n/2) × b^(n mod 2)
```

Exemplo de 2 elevado a 8:

```text
2⁸ = 2⁴ × 2⁴     → preciso calcular 2⁴
2⁴ = 2² × 2²     → preciso calcular 2²
2² = 2 × 2       → fácil, é 4
```

Exemplo de 2 elevado a 5:

```text
2⁵ = 2² × 2² × 2    → divido por 2 e multiplico por 2 no final
2² = 2 × 2          → é 4
```

---

## Análise de complexidade

```text
T(n) = T(n/2) + 1
T(n/2) = T(n/4) + 1
T(n/4) = T(n/8) + 1
...
```

## Comparando os métodos:

| Expoente | Tradicional | Square & Multiply |
|----------|-------------|-------------------|
| 10       | 9           | 4                 |
| 100      | 99          | ~7                |
| 1000     | 999         | ~10               |

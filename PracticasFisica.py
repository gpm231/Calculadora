vals = []

amountOfVals = int(input())

for i in range(amountOfVals):
    vals.append(float(input()))

def avg(vals):
    total = 0

    for i, v in enumerate(vals):
        total += v

    return total / len(vals)

def disp(vals, average):
    return (max(vals) - min(vals)) / average * 100

def unc_abs(vals):
    return (max(vals) - min(vals)) / 2

def unc_rel(abs_unc, average):
    return (abs_unc / average) * 100

average = avg(vals)
dispersion = disp(vals, average)
absoluteUncertainty = unc_abs(vals)
relativeUncertainty = unc_rel(absoluteUncertainty, average)

print("Media = " + str(round(average, 5)))
print("Dispersion = " + str(round(dispersion, 5)) + "%")
print("Incertidumbre absoluta = " + str(round(absoluteUncertainty, 5)))
print("Incertidumbre relativa = " + str(round(relativeUncertainty, 5)) + "%")
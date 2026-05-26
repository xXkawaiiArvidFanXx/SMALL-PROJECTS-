import random
import matplotlib.pyplot as plt
def simulera_tarningar(antal_tarningar=10, antal_kast=100):
    tarning_summa = [sum(random.randint(1, 6) for _ in range(antal_tarningar)) for _ in range(antal_kast)]
    return tarning_summa
def plotta_fordelning(tarning_summa, antal_tarningar=10):
    bins = range(antal_tarningar, 6 * antal_tarningar + 2)
    plt.hist(tarning_summa, bins=bins, density=True, alpha=0.6, color='g', edgecolor='black')
    plt.title(f'Fördelning av summan av {antal_tarningar} tärningar')
    plt.xlabel('Summa av tärningarna')
    plt.ylabel('Sannolikhet')
    plt.grid(True)
    plt.show()
if __name__ == '__main__':
    resultat = simulera_tarningar(10, 100)
    print('Antal kast:', len(resultat))
    print('Alla summor:', resultat[:100])
    plotta_fordelning(resultat, 10)

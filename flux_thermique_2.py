import numpy as np
import matplotlib.pyplot as plt

# Paramètres physiques
k = 1.0  # Conductivité thermique
q = 1.0  # Source de chaleur
Lx, Ly = 1.0, 1.0  # Dimensions de la plaque

# Paramètres du maillage
Nx, Ny = 50, 50  # Nombre de nœuds dans chaque direction
dx, dy = Lx / (Nx - 1), Ly / (Ny - 1)  # Taille des éléments

# Nombre total de nœuds
N = Nx * Ny

# Construction de la matrice de conductivité et du vecteur des forces
K = np.zeros((N, N))  # Matrice de conductivité
F = np.zeros(N)       # Vecteur des forces
T = np.zeros(N)       # Vecteur des températures

# Assemblage de la matrice de conductivité et du vecteur des forces
for i in range(N):
    xi, yi = i % Nx, i // Nx  # Indices x et y du nœud i
    for j in range(N):
        xj, yj = j % Nx, j // Nx  # Indices x et y du nœud j
        if i == j:
            # Contribution locale : diagonale (sommation des connexions)
            K[i, j] = -4 * k / dx**2
        elif abs(xi - xj) + abs(yi - yj) == 1:
            # Nœuds adjacents : contribution hors diagonale
            K[i, j] = k / dx**2

    # Source de chaleur au nœud i
    F[i] = q * dx * dy

# Conditions aux limites : température fixe (Dirichlet)
for i in range(N):
    xi, yi = i % Nx, i // Nx
    if xi == 0 or xi == Nx - 1 or yi == 0 or yi == Ny - 1:
        K[i, :] = 0
        K[i, i] = 1
        F[i] = 0  # Température fixée à 0 sur les bords

# Résolution du système linéaire
T = np.linalg.solve(K, F)

# Reshape pour une visualisation 2D
T_2D = T.reshape((Ny, Nx))

# Affichage des résultats
plt.imshow(T_2D, origin='lower', extent=[0, Lx, 0, Ly], cmap='hot')
plt.colorbar(label='Température (K)')
plt.title('Distribution de température (MEF avec NumPy)')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.show()

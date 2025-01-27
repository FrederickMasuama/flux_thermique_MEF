import numpy as np
import matplotlib.pyplot as plt


#Méthode de resolution itérative: Gauss-Seidel
def gauss_seidel(A, b, x, max_iter, tol):
    M = np.diag(np.diag(A)) + np.tril(A, k=-1)
    N = - np.triu(A, k=1)
    M_inv = np.linalg.inv(M)
    num_iter = 0

    for i in range(max_iter):
        x_new = ( M_inv @ N ) @ x + M_inv @ b #itérations
        num_iter += 1

        """conditions d'arrêt"""
        if np.linalg.norm(x_new - x, ord = 2) < tol:
            break
        if num_iter == max_iter :
            print("Nous avons atteint le nombre max d'itérations sans convergence")

        x = x_new
        
    return [x, num_iter]

# Paramètres physiques
k = 1.0  # Conductivité thermique
q = 1.0  # Source de chaleur
Lx, Ly = 1.0, 1.0  # Dimensions de la plaque

# Paramètres du maillage
Nx, Ny = 25, 25  # Nombre de nœuds dans chaque direction (pour faire le maillage)
dx, dy = Lx / (Nx - 1), Ly / (Ny - 1)  # Taille des éléments

# Nombre total de nœuds
N = Nx * Ny

# Construction de la matrice de conductivité et du vecteur des forces
""" On sait que la MEF nous donne l'équation matricielle: K.T = F """
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
"""Par linalg.solve"""
#T = np.linalg.solve(K, F)

"""Par Gauss-Seidel"""
max_iter = 1000
tol = 1e-6
x = np.zeros_like(F , dtype = float)

sol_T = gauss_seidel(K, F, x, max_iter, tol)
T = sol_T[0]

# Reshape pour une visualisation 2D
T_2D = T.reshape((Ny, Nx))

# Affichage des résultats
plt.imshow(T_2D, origin='lower', extent=[0, Lx, 0, Ly], cmap='hot')
plt.colorbar(label='Température (K)')
plt.title('Distribution de température (MEF avec NumPy)')
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.show()


import noise
import numpy as np
import matplotlib.pyplot as plt

def generate_leather_texture(width, height, scale=100, octaves=5, persistence=0.5, lacunarity=2.0, seed=None):
    if seed is not None:
        np.random.seed(seed)

    # Generate a random noise grid
    grid = np.random.rand(width, height)

    # Create a 2D grid of coordinates
    x = np.linspace(0, 1, width, endpoint=False) * scale
    y = np.linspace(0, 1, height, endpoint=False) * scale
    x_grid, y_grid = np.meshgrid(x, y)

    # Generate Perlin noise using NumPy's vectorized operations
    pnoise2_vec = np.vectorize(noise.pnoise2)
    noise_grid = pnoise2_vec(x_grid / scale, y_grid / scale, octaves=octaves, persistence=persistence, lacunarity=lacunarity)

    # Add the generated noise to the grid
    grid += noise_grid

    # Normalize the values to the range [0, 1]
    grid = (grid - grid.min()) / (grid.max() - grid.min())

    return grid

def plot_texture(texture):
    plt.imshow(texture, cmap='gray', interpolation='bicubic', extent=[0, 1, 0, 1])
    plt.axis('off')

    # Set aspect ratio to be equal and specify figure size
    fig = plt.gcf()
    fig.set_size_inches(width / 100, height / 100)
    plt.gca().set_axis_off()
    
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())
    plt.savefig("leather_texture.png", format='png', bbox_inches='tight', pad_inches=0, dpi=300)
    plt.show()

if __name__ == "__main__":
    width, height = 512, 512
    leather_texture = generate_leather_texture(width, height)
    plot_texture(leather_texture)
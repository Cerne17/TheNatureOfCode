import matplotlib.pyplot as plt
from perlin_noise import PerlinNoise

noise = PerlinNoise(octaves=10, seed=1)

xSize, ySize = 100, 100
picture = [[noise([j/xSize, i/ySize]) for j in range(ySize)] for i in range(xSize)]

plt.imshow(picture, cmap='gray')
plt.show()


noise1 = PerlinNoise(octaves=3)
noise2 = PerlinNoise(octaves=6)
noise3 = PerlinNoise(octaves=12)
noise4 = PerlinNoise(octaves=24)
noise5 = PerlinNoise(octaves=48)
noise6 = PerlinNoise(octaves=96)

picture = []

for i in range(xSize):
    row = []
    for j in range(ySize):
        noise_val = noise1([i/xSize, j/ySize])
        noise_val += 0.5 * noise2([i/xSize, j/ySize])
        noise_val += 0.25 * noise3([i/xSize, j/ySize])
        noise_val += 0.125 * noise4([i/xSize, j/ySize])
        noise_val += 0.125/2 * noise5([i/xSize, j/ySize])
        noise_val += 0.125/4 * noise6([i/xSize, j/ySize])
        row.append(noise_val)
    picture.append(row)

plt.imshow(picture, cmap='gray')
plt.show()

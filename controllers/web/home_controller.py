from flask import request, redirect, url_for
from traits import render, view
import io
import base64
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from traits.query_builder import QueryBuilder

class HomeController:

  def index(self):
    return render(view('home/index'))
    
  def plot2d(self):
    data = {
      'scatter': self.scatter_plot(),
      'line': self.line_plot(),
      'bar': self.bar_plot(),
      'fill_between': self.fill_between_plot()
    }

    return render(view('plot2d/index'), data=data)

  def plot3d(self):
    data = {
      'scatter3d': self.scatter_plot3d(),
      'surface': self.surface_plot(),
      'trisurf': self.trisurf_plot(),
      'voxels': self.voxels_plot()
    }

    return render(view('plot3d/index'), data=data)
  
  def scatter_plot(self):  # Add self as the first parameter
    # Data dummy
    x = np.random.randint(20, size=20)
    y = np.random.randint(20, size=20)

    # Membuat scatter plot menggunakan Matplotlib
    plt.scatter(x, y)
    plt.xlabel('X Axis')
    plt.ylabel('Y Axis')
    plt.title('Scatter Plot')

    # Simpan gambar ke buffer
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode gambar ke dalam base64
    encoded_img = base64.b64encode(img.getvalue()).decode('utf-8')

    # Hapus plot agar tidak terakses lagi
    plt.clf()

    return encoded_img

  def scatter_plot3d(self):  # Add self as the first parameter
    np.random.seed(19680801)
    n = 100
    rng = np.random.default_rng()
    xs = rng.uniform(23, 32, n)
    ys = rng.uniform(0, 100, n)
    zs = rng.uniform(-50, -25, n)

    # Plot
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.scatter(xs, ys, zs)

    ax.set(xticklabels=[],
          yticklabels=[],
          zticklabels=[])

    # Simpan gambar ke buffer
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode gambar ke dalam base64
    encoded_img = base64.b64encode(img.getvalue()).decode('utf-8')

    # Hapus plot agar tidak terakses lagi
    plt.clf()

    return encoded_img
  
  def fill_between_plot(self):  # Add self as the first parameter
    np.random.seed(1)
    x = np.linspace(0, 8, 16)
    y1 = 3 + 4*x/8 + np.random.uniform(0.0, 0.5, len(x))
    y2 = 1 + 2*x/8 + np.random.uniform(0.0, 0.5, len(x))

    # plot
    fig, ax = plt.subplots()

    ax.fill_between(x, y1, y2, alpha=.5, linewidth=0)
    ax.plot(x, (y1 + y2)/2, linewidth=2)

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
          ylim=(0, 8), yticks=np.arange(1, 8))

    # Simpan gambar ke buffer
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode gambar ke dalam base64
    encoded_img = base64.b64encode(img.getvalue()).decode('utf-8')

    # Hapus plot agar tidak terakses lagi
    plt.clf()

    return encoded_img
  
  def bar_plot(self):  # Add self as the first parameter
    # Data dummy
    x = 0.5 + np.arange(8)
    y = [4.8, 5.5, 3.5, 4.6, 6.5, 6.6, 2.6, 3.0]

    # plot
    fig, ax = plt.subplots()

    ax.bar(x, y, width=1, edgecolor="white", linewidth=0.7)

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
          ylim=(0, 8), yticks=np.arange(1, 8))

    # Simpan gambar ke buffer
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode gambar ke dalam base64
    encoded_img = base64.b64encode(img.getvalue()).decode('utf-8')

    # Hapus plot agar tidak terakses lagi
    plt.clf()

    return encoded_img
  
  def line_plot(self):  # Add self as the first parameter
    # Data dummy
    x = np.linspace(0, 10, 100)
    y = 4 + 2 * np.sin(2 * x)

    # plot
    fig, ax = plt.subplots()

    ax.plot(x, y, linewidth=2.0)

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
          ylim=(0, 8), yticks=np.arange(1, 8))

    # Simpan gambar ke buffer
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode gambar ke dalam base64
    encoded_img = base64.b64encode(img.getvalue()).decode('utf-8')

    # Hapus plot agar tidak terakses lagi
    plt.clf()

    return encoded_img

  def voxels_plot(self):  # Add self as the first parameter
    # Data dummy
    x, y, z = np.indices((8, 8, 8))

    # Draw cuboids in the top left and bottom right corners
    cube1 = (x < 3) & (y < 3) & (z < 3)
    cube2 = (x >= 5) & (y >= 5) & (z >= 5)

    # Combine the objects into a single boolean array
    voxelarray = cube1 | cube2

    # Plot
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.voxels(voxelarray, edgecolor='k')

    ax.set(xticklabels=[],
          yticklabels=[],
          zticklabels=[])

    # Simpan gambar ke buffer
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode gambar ke dalam base64
    encoded_img = base64.b64encode(img.getvalue()).decode('utf-8')

    # Hapus plot agar tidak terakses lagi
    plt.clf()

    return encoded_img
  
  def surface_plot(self):  # Add self as the first parameter
    # Data dummy
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)

    # Plot the surface
    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap=cm.Blues)

    ax.set(xticklabels=[],
          yticklabels=[],
          zticklabels=[])

    # Simpan gambar ke buffer
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode gambar ke dalam base64
    encoded_img = base64.b64encode(img.getvalue()).decode('utf-8')

    # Hapus plot agar tidak terakses lagi
    plt.clf()

    return encoded_img

  def trisurf_plot(self):  # Add self as the first parameter
    # Data dummy
    n_radii = 8
    n_angles = 36 
    radii = np.linspace(0.125, 1.0, n_radii)
    angles = np.linspace(0, 2*np.pi, n_angles, endpoint=False)[..., np.newaxis]

    # Convert polar (radii, angles) coords to cartesian (x, y) coords.
    x = np.append(0, (radii*np.cos(angles)).flatten())
    y = np.append(0, (radii*np.sin(angles)).flatten())
    z = np.sin(-x*y)

    # Plot
    fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
    ax.plot_trisurf(x, y, z, vmin=z.min() * 2, cmap=cm.Blues)

    ax.set(xticklabels=[],
          yticklabels=[],
          zticklabels=[])

    # Simpan gambar ke buffer
    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    # Encode gambar ke dalam base64
    encoded_img = base64.b64encode(img.getvalue()).decode('utf-8')

    # Hapus plot agar tidak terakses lagi
    plt.clf()

    return encoded_img

  # def generate_plot(self):  # Add self as the first parameter
  #   # Data dummy
  #   x = [1, 2, 3, 4, 5]
  #   y = [2, 3, 5, 7, 11]

  #   # Membuat scatter plot menggunakan Matplotlib
  #   plt.scatter(x, y)
  #   plt.xlabel('X Axis')
  #   plt.ylabel('Y Axis')
  #   plt.title('Scatter Plot')

  #   # Simpan gambar sebagai file
  #   filename = 'static/figs/plot.png'
  #   plt.savefig(filename, format='png')

  #   # Hapus plot agar tidak terakses lagi
  #   plt.clf()

  #   return filename
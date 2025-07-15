import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from Model.generarCami import generarCami

G = nx.petersen_graph()

pos = {
    0: (0, 1), 1: (0.951, 0.309), 2: (0.588, -0.809),
    3: (-0.588, -0.809), 4: (-0.951, 0.309),
    5: (0, 0.5), 6: (0.475, 0.154), 7: (0.294, -0.404),
    8: (-0.294, -0.404), 9: (-0.475, 0.154)
}

path = generarCami(G)
if not path:
    print("No s'ha trobat cap camí hamiltonià.")
    exit()

print("Camí trobat:", path)

fig, ax = plt.subplots(figsize=(7, 7))
nx.draw(G, pos, with_labels=True, node_color='lightblue',
        edge_color='gray', node_size=800, font_weight='bold', ax=ax)
line, = ax.plot([], [], color='red', linewidth=3)

coords = [pos[node] for node in path]

fig_text = fig.text(0.5, 0.03, "", ha='center', fontsize=12)

def init():
    line.set_data([], [])
    fig_text.set_text("")
    return line, fig_text

def update(i):
    x = [coord[0] for coord in coords[:i+1]]
    y = [coord[1] for coord in coords[:i+1]]
    line.set_data(x, y)

    partial_path = path[:i+1]
    fig_text.set_text("Camí: " + " → ".join(map(str, partial_path)))
    return line, fig_text

ani = animation.FuncAnimation(
    fig, update, frames=len(coords), init_func=init,
    blit=False, interval=800, repeat=False
)

plt.title("Construcció animada d'un camí Hamiltonià")
plt.axis('equal')
plt.tight_layout()
plt.show()

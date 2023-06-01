from pysmiles import read_smiles
import networkx as nx
import matplotlib.pyplot as plt

# a = read_smiles("C12=C3C4=C5C6=C1C7=C8C9=C1C%10=C%11C(=C29)C3=C2C3=C4C4=C5C5=C9C6=C7C6=C7C8=C1C1=C8C%10=C%10C%11=C2C2"
#                 "=C3C3=C4C4=C5C5=C%11C%12=C(C6=C95)C7=C1C1=C%12C5=C%11C4=C3C3=C5C(=C81)C%10=C23")
a = read_smiles("OCCc1c(C)[n+](cs1)Cc2cnc(C)nc2N")

print(a)

# atom vector (C only)
print(a.nodes(data='element'))
# adjacency matrix
print(nx.to_numpy_matrix(a))


elements = nx.get_node_attributes(a, name="element")
nx.draw(a, with_labels=True, labels=elements, pos=nx.spring_layout(a))
plt.gca().set_aspect('equal')

plt.show()

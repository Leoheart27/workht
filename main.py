class Estado: # Elemento da lista encadeada
    def __init__(self, siglaEstado=None, nomeEstado=None):
        self.siglaEstado = siglaEstado
        self.nomeEstado = nomeEstado
        self.next = None

class LinkedList: # Lista encadeada
    def __init__(self):
        self.head = None

    def insert(self, siglaEstado, nomeEstado): # insere o nodo na lista encadeada
        node = Estado(siglaEstado, nomeEstado)
        if self.head == None:
            self.head = node
            return
        
        else:
            node.next = self.head
            self.head = node
            return
            
        
    def printList(self, index): # Imprime cada nodo dentro da lista
        temp = self.head
        node_str = ""
        while temp:
            node_str += f"{temp.siglaEstado}"
            if temp.next:
                node_str += " -> "
            else:
                node_str += " -> None"
            temp = temp.next
        if self.head == None:
            node_str = 'None'
            
        print(f"{index}: {node_str}")


class HashTable: # Tabela Hash
    def __init__(self):
        self.size = 10
        self.table = [LinkedList() for i in range(0, self.size)]

    def hashFunction(self, siglaEstado): # função hash
        if siglaEstado == 'DF':
            return 7
        siglaEstado = list(siglaEstado)
        return (ord(siglaEstado[0]) + ord(siglaEstado[1])) % self.size
    
    def insert(self, siglaEstado, nomeEstado): # função de inserção do lista encadeada na tabela
        index = self.hashFunction(siglaEstado)
        self.table[index].insert(siglaEstado, nomeEstado)
    
    def printTable(self): # Imprime a tabela
        for i in range(self.size):
            self.table[i].printList(i)


hash_table = HashTable()

# Região Norte
hash_table.insert('AC', 'Acre')
hash_table.insert('AP', 'Amapá')
hash_table.insert('AM', 'Amazonas')
hash_table.insert('PA', 'Pará')
hash_table.insert('RO', 'Rondônia')
hash_table.insert('RR', 'Roraima')
hash_table.insert('TO', 'Tocantins')

# Região Nordeste
hash_table.insert('AL', 'Alagoas')
hash_table.insert('BA', 'Bahia')
hash_table.insert('CE', 'Ceará')
hash_table.insert('MA', 'Maranhão')
hash_table.insert('PB', 'Paraíba')
hash_table.insert('PE', 'Pernambuco')
hash_table.insert('PI', 'Piauí')
hash_table.insert('RN', 'Rio Grande do Norte')
hash_table.insert('SE', 'Sergipe')

# Região Centro-Oeste
hash_table.insert('DF', 'Distrito Federal')
hash_table.insert('GO', 'Goiás')
hash_table.insert('MT', 'Mato Grosso')
hash_table.insert('MS', 'Mato Grosso do Sul')

# Região Sudeste
hash_table.insert('ES', 'Espírito Santo')
hash_table.insert('MG', 'Minas Gerais')
hash_table.insert('RJ', 'Rio de Janeiro')
hash_table.insert('SP', 'São Paulo')

# Região Sul
hash_table.insert('PR', 'Paraná')
hash_table.insert('RS', 'Rio Grande do Sul')
hash_table.insert('SC', 'Santa Catarina')

# Inserindo meu nome completo
hash_table.insert('LC', 'Leonardo da Silva Paiva da Costa')

hash_table.printTable()

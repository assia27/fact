
id_clients = 1

def client_exist(clients, nom, prenom):
	for client in clients:
		if client['nom'] == nom and client['prenom'] == prenom:
			return True
	return False
	
def entrer_client(id_client):
	client = {'id': '','nom': '', 'prenom': '', 'adresse': ''}
	client['id'] = id_client
	client['nom'] = raw_input('Entrer le nom: ')
	client['prenom'] = raw_input('Entrer le prenom: ')
	client['adresse'] = raw_input('Entrer addresse: ')
	return client

clients = []
clients.append(entrer_client(id_clients)) # ajouter a la fin de la liste
id_clients = id_clients + 1
clients.append(entrer_client(id_clients)) # ajouter a la fin de la liste
id_clients = id_clients + 1

def entrer_produit():
	produit = {'id': '','desiniation': '', 'prix_unitair': ''}
	produit['id'] = raw_input('Entrer le ...: ')
	produit['desiniation'] = raw_input('Entrer le ...: ')
	produit['prix_unitair'] = raw_input('Entrer ...: ')
	return produit

produits = []
produits.append(entrer_produit()) # ajouter a la fin de la liste

def fonction1():
	print '---------------------'
	print 'Liste des Clients: '
	print '---------------------'
	for client in clients:
		print '{0} {1} {2}'.format(str(client['id']), client['nom'], client['prenom'])
	print '---------------------'
	print 'choix du client: '	
	print '---------------------'
	new_nom = raw_input('Entrer le nom du client: ')
	new_prenom = raw_input('Entrer le prenom du client: ')
	if not client_exist(clients, new_nom, new_prenom):
		client = {'id': id_clients, 'nom': new_nom, 'prenom': new_prenom, 'adresse': ''}
		client['adresse'] = raw_input('Entrer addresse: ')
		clients.append(client)
	
	print '--------------------'
	print 'Entrer num de la facture: '
	print '--------------------'
	num_facture = raw_input('')
	
	print '--------------------'
	print 'Entrer la Date: '
	print '--------------------'
	jour = raw_input('entrer le jour: ')
	mois = raw_input('entrer le mois: ')
	annee = raw_input('entrer le annee: ')
	
	print '---------------------'
	print 'Liste des Produits: '
	print '---------------------'
	for produit in produits:
		print '{0} {1} {2}'.format(str(produit['id']), produit['desiniation'], produit['prix_unitair'])
	print '---------------------'
	print 'choix des produits: '	
	print '---------------------'
	list_produits= []
	while 1:
		i = raw_input('id> ')
		if i == 'Q':
			break
		ii = raw_input('quantite> ')
		x = False
		for produit in produits:
			if produit['id'] == i:
				x = True
				break
		if x:
			list_produits.append((int(i), int(ii)))
		else:
			print 'le produit n existe pas'
			
	print list_produits
	
	print '---------------------'
	print 'choix la taxe: '	
	print '---------------------'
	taxe = raw_input('Entrer la taxe: ')
	
	return (new_nom, new_prenom, num_facture, (jour, mois, annee), list_produits, int(taxe))
	
"""print 'nom = ' + clients[0]['nom']
print 'id = ' + str(clients[0]['id'])"""


"""if client_exist(clients, 'qsd', 'dqq'):
	print 'ok'
else :
	print 'No'"""
	
res = fonction1()
id_clients = clients[-1]['id'] + 1

print 'nom = ' + res[0]
print 'prenom = ' + res[1]
print 'num_facture = ' + res[2]
print  res[4]

def totaux(lists_produits):
	t = []
	for i in lists_produits:
		prix = 0
		for j in produits:
			if int(i[0]) == int(j['id']):
				prix = j['prix_unitair']
				break
		montant = int(i[1]) * int(prix)
		t.append(int(montant))
	return t

qsd = totaux(res[4])

print qsd		

print sum(qsd)

print float(float(sum(qsd) * res[5])/100 + sum(qsd))
 
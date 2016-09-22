
id_clients = 1

def client_exist(clients, nom, prenom):
	for client in clients:
		if client['nom'] == nom and client['prenom'] == prenom:
		    return True
	return False
	
def entrer_client(id_client): #input clients
	client = {'id': '','nom': '', 'prenom': '', 'adresse': ''}
	client['id'] = id_client
	client['nom'] = raw_input('Entrer le nom du client : ')
	client['prenom'] = raw_input('Entrer le prenom du client: ')
	client['adresse'] = raw_input('Entrer son addresse svp: ')
	return client

clients = []
clients.append(entrer_client(id_clients)) # ajouter a la fin de la liste
id_clients = id_clients + 1
clients.append(entrer_client(id_clients)) # ajouter a la fin de la liste
id_clients = id_clients + 1

def entrer_produit():  # input produits
	produit = {'id': '','desiniation': '', 'prix_unitair': ''}
	produit['id'] = raw_input('Entrer l\'identificateur de produit: ')
	produit['desiniation'] = raw_input('Entrer sa designation : ')
	produit['prix_unitair'] = raw_input('Entrer son prix unitaire: ')
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
		client['adresse'] = raw_input('le client n\'existe pas entrer son adresse svp pour le rajoute a la liste: ')
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
	#list_p = list_produits
	
	print 'veuillez inserer les produits demander et quand vous allez terminer entre Q pour quitte l\'insertion'
	
	while 1:
		i = raw_input('id=> ')
		if i == 'Q' or i == 'q' :
			break
		ii = raw_input('quantite=> ')
		x = False
		for produit in produits:
			if produit['id'] == i:
				x = True
				break
		if x:
			list_produits.append((int(i), int(ii)))
		else:
			print 'desole veuillez inserer un autre produit a partir de la liste des produits au-dessus celui la n\'existe pas dans le stock'
			
	print list_produits #+ list_p
	
	print '---------------------'
	print 'choix la taxe: '	
	print '---------------------'
	taxe = raw_input('Entrer la taxe: ')
	
	return (new_nom, new_prenom, num_facture, (jour , mois , annee), list_produits, int(taxe))
	
"""print 'nom = ' + clients[0]['nom']
print 'id = ' + str(clients[0]['id'])"""


"""if client_exist(clients, 'qsd', 'dqq'):
	print 'ok'
else :
	print 'No'"""
	
res = fonction1()
id_clients = clients[-1]['id'] + 1

print '************************************/  Facture  /*******************************'
print '_________________________________________________'
print '|     nom du client :       ' + res[0] + '             |' 
print '|     prenom du client :    ' + res[1] + '               |'
print '|     numero de facture :   ' + res[2] + '               |'
print '|     la date :             ' + str(res[3])+ '|'
print '-------------------------------------------------' 
print '********************************************************************************'
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

ST = totaux(res[4])

print 'les sous totaux :    ' + str(ST)		

print 'Le Total global HT : ' + str(sum(ST)) + 'DA'

print 'TTC :              ' + str(float(float(sum(ST) * res[5])/100 + sum(ST))) + 'DA'

print produits 

print res[4]
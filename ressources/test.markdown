# Meeting du 21/06/2016

* profiter de 
* écrire le programme en prenant en compte **Store Wizzard** et **SAP**

Commencer par déployer pour tous le monde et voir ensuite ce qu'il faut pour les autres pays (sous forme de Plugin).

Reunion mercredi prochain avec Gilles Vueberg


## Store Wizzard

* Les prix Store Wizzard evoluent constament donc il faut trouver une solution pour qu'ils soient rentré automatiquement
  * Connection StoreWizzard -> Caméléon auto (pas obligatoire)

* déduire les code en fonction des couleur `'26ao46{color}`

~~~mermaid
graph TD;

subgraph Store Wizzard
	c_wiz1(cabinet)
	c_wiz2(cabinet)
	c_wiz3(cabinet)
	c_wiz4(cabinet)
end

subgraph Configurateur
	l_conf(Linéaire)
end

l_conf --> c_wiz1
l_conf --> c_wiz2
l_conf --> c_wiz3
l_conf --> c_wiz4 



~~~

### Données

Guillaume accède aux données via StoreWizzard via une **table Access**. Il vérifie lui même les informations  (via le CoolNet):

* Gabriel Rua (mec à la tête de StoreWizzard)
* Gabriel Eolaf (celui qui met à jour StoreWizzard)

### Prix 

Les prix sur Store Wizzard sont en GWP , la remise change en fonction:

* de l'enseigne
* de la gamme de meuble

~~~mermaid
graph TD;


GWP--remise-->prix_Carrier
prix_Carrier--coef 1,035 ou 1,118-->prix_revient
prix_revient--frais annexes*-->prix_client

	prix_Carrier-->prix_public
	prix_public--remise-->prix_client


~~~
*Frais annexes:

* transports
* pièces spécifiques (portes allu, tablettes,etc..)

### système

~~~mermaid
graph TD;


Cameleon-->Enseigne
Enseigne--referencement-->Choix_des_meubles


~~~

### Spécial

Les demandes de spécial sont demandé au **Poduct Management** qui crée un nouveau code en `SPA_{}`


## Objectif

* Calcul de la consommation globale sur la totalité du magasin 
  * avec ou sans portes
  * génère le retour sur investissement
* paramètres global pour tout le magasin pour simplifier la configuration
  * couleur 
  * régulation


~~~mermaid

graph TD;

subgraph Databases
	LSA
	Client
	Other
end

LSA-->CRM
Client-->CRM
Other-->CRM

CRM--préremplis-->Configurateur

3D
SAP

~~~

## Sketchup